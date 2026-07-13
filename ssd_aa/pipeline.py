"""Orquesta todo el flujo: datos reales -> features -> modelos -> métricas
PRE/POST -> catálogo enriquecido -> tabla única de predicción/recomendación/riesgo
que consume la app de Streamlit."""

import time
from dataclasses import dataclass, field

import pandas as pd

from ssd_aa.baseline import forecast_naive
from ssd_aa.catalog import catalog_by_titulo_bd_ventas
from ssd_aa.config import (
    PRINT_RUN_SAFETY_BUFFER,
    RISK_LOW_MAX_DEVIATION,
    RISK_MEDIUM_MAX_DEVIATION,
)
from ssd_aa.data import aggregate_monthly, load_raw
from ssd_aa.features import FEATURE_COLUMNS, build_features, rows_with_full_history
from ssd_aa.metrics import mape, overstock_pct, recommend_print_run, risk_level, stockout_pct
from ssd_aa.models import save_winner, select_winner, time_based_split, train_and_compare


@dataclass
class PipelineResult:
    modelos: dict
    modelo_ganador: str
    metadata_modelo: dict
    metricas_pre: dict
    metricas_post: dict
    comparacion_modelos: pd.DataFrame
    resumen_titulos: pd.DataFrame
    tiempo_total_seg: float
    df_test: pd.DataFrame = field(repr=False)
    df_features: pd.DataFrame = field(repr=False)
    modelo_activo: object = field(repr=False)


def _comparar_modelos_df(resultados: dict) -> pd.DataFrame:
    filas = [
        {
            "modelo": nombre,
            "mape": r["mape"],
            "mae": r["mae"],
            "rmse": r["rmse"],
            "tiempo_entrenamiento_seg": r["tiempo_entrenamiento_seg"],
        }
        for nombre, r in resultados.items()
    ]
    return pd.DataFrame(filas).sort_values("mape").reset_index(drop=True)


def _resumen_por_titulo(df_features_full: pd.DataFrame, modelo, mape_test: float) -> pd.DataFrame:
    """Una fila por título: demanda prevista (próximo mes), tiraje recomendado,
    stock actual estimado (proxy) y nivel de riesgo."""
    es_pronostico = df_features_full["ventas"].isna() & df_features_full[FEATURE_COLUMNS].notna().all(axis=1)
    filas_pronostico = df_features_full.loc[es_pronostico].sort_values("fecha")
    filas_pronostico = filas_pronostico.drop_duplicates(subset="titulo", keep="first")

    demanda_prevista = modelo.predict(filas_pronostico[FEATURE_COLUMNS])
    ultima_venta_real = filas_pronostico["lag_1"]  # venta real del mes inmediato anterior al pronóstico

    confianza = max(0.0, 100.0 - mape_test)

    resumen = pd.DataFrame({
        "titulo": filas_pronostico["titulo"].values,
        "fecha_pronostico": filas_pronostico["fecha"].values,
        "demanda_prevista": demanda_prevista,
        "stock_actual_estimado": recommend_print_run(ultima_venta_real.values, PRINT_RUN_SAFETY_BUFFER),
    })
    resumen["tiraje_recomendado"] = recommend_print_run(resumen["demanda_prevista"], PRINT_RUN_SAFETY_BUFFER)
    resumen["riesgo"] = [
        risk_level(dp, ref, RISK_LOW_MAX_DEVIATION, RISK_MEDIUM_MAX_DEVIATION)
        for dp, ref in zip(resumen["demanda_prevista"], resumen["stock_actual_estimado"])
    ]
    resumen["confianza_modelo"] = confianza
    return resumen.set_index("titulo")


def run_pipeline() -> PipelineResult:
    inicio = time.perf_counter()

    crudo = load_raw()
    mensual = aggregate_monthly(crudo)
    df_features = build_features(mensual)
    df_hist = rows_with_full_history(df_features)

    df_train, df_test = time_based_split(df_hist)
    resultados = train_and_compare(df_train, df_test)
    ganador = select_winner(resultados)
    save_winner(ganador, resultados)
    modelo_activo = resultados[ganador]["modelo"]

    pronostico_baseline = forecast_naive(df_test)
    tiraje_baseline = recommend_print_run(pronostico_baseline)
    metricas_pre = {
        "mape": mape(df_test["ventas"], pronostico_baseline),
        "sobrestock_pct": overstock_pct(df_test["ventas"], tiraje_baseline),
        "quiebre_pct": stockout_pct(df_test["ventas"], tiraje_baseline),
    }

    pronostico_modelo = modelo_activo.predict(df_test[FEATURE_COLUMNS])
    tiraje_modelo = recommend_print_run(pronostico_modelo)
    metricas_post = {
        "mape": mape(df_test["ventas"], pronostico_modelo),
        "sobrestock_pct": overstock_pct(df_test["ventas"], tiraje_modelo),
        "quiebre_pct": stockout_pct(df_test["ventas"], tiraje_modelo),
    }

    resumen_titulos = _resumen_por_titulo(df_features, modelo_activo, resultados[ganador]["mape"])
    resumen_titulos = resumen_titulos.join(catalog_by_titulo_bd_ventas(), how="left")

    tiempo_total = time.perf_counter() - inicio

    return PipelineResult(
        modelos=resultados,
        modelo_ganador=ganador,
        metadata_modelo={"nombre": ganador, "mape_test": resultados[ganador]["mape"]},
        metricas_pre=metricas_pre,
        metricas_post=metricas_post,
        comparacion_modelos=_comparar_modelos_df(resultados),
        resumen_titulos=resumen_titulos.reset_index(),
        tiempo_total_seg=tiempo_total,
        df_test=df_test,
        df_features=df_features,
        modelo_activo=modelo_activo,
    )


if __name__ == "__main__":
    resultado = run_pipeline()
    print(f"Modelo ganador: {resultado.modelo_ganador}\n")
    print("Comparación de modelos:")
    print(resultado.comparacion_modelos.to_string(index=False))
    print()
    print("PRE (método empírico / media móvil 3 meses):", resultado.metricas_pre)
    print("POST (modelo ganador):", resultado.metricas_post)
    print()
    print(f"Tiempo total del pipeline: {resultado.tiempo_total_seg:.2f} s")
    print()
    print("Resumen por título (primeras filas):")
    print(resultado.resumen_titulos[
        ["titulo", "demanda_prevista", "tiraje_recomendado", "stock_actual_estimado", "riesgo"]
    ].head(10).to_string(index=False))
