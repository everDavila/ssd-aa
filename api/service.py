"""Transforma PipelineResult / DataFrames a las formas JSON de schemas.py.
Ninguna métrica se recalcula aquí: todo viene de ssd_aa.pipeline/catalog/explain."""

import io
import math

import numpy as np
import pandas as pd

from ssd_aa import config
from ssd_aa.catalog import load_catalog
from ssd_aa.explain import compute_feature_importance
from ssd_aa.features import FEATURE_COLUMNS
from ssd_aa.metrics import recommend_print_run
from ssd_aa.pipeline import PipelineResult


def _none_if_nan(value):
    if value is None:
        return None
    if isinstance(value, float) and math.isnan(value):
        return None
    return value


def _serie_from_df(df: pd.DataFrame) -> list[dict]:
    return [
        {"fecha": fecha.date().isoformat(), "ventas": float(ventas)}
        for fecha, ventas in zip(df["fecha"], df["ventas"])
    ]


def get_dashboard(resultado: PipelineResult) -> dict:
    pre, post = resultado.metricas_pre, resultado.metricas_post
    resumen = resultado.resumen_titulos

    top = resumen.sort_values("demanda_prevista", ascending=False)
    titulo_lider = top["titulo"].iloc[0]

    historial = resultado.df_features[
        (resultado.df_features["titulo"] == titulo_lider) & resultado.df_features["ventas"].notna()
    ][["fecha", "ventas"]].sort_values("fecha")

    catalogo = load_catalog()

    return {
        "kpis": {
            "mape_actual": post["mape"],
            "mape_delta": post["mape"] - pre["mape"],
            "sobrestock_pct": post["sobrestock_pct"],
            "sobrestock_delta": post["sobrestock_pct"] - pre["sobrestock_pct"],
            "quiebre_pct": post["quiebre_pct"],
            "quiebre_delta": post["quiebre_pct"] - pre["quiebre_pct"],
            "tiempo_proceso_seg": resultado.tiempo_total_seg,
        },
        "top_riesgo": top.head(6)[["id_titulo", "titulo", "demanda_prevista", "riesgo"]].to_dict(orient="records"),
        "chart_demanda": {"titulo": titulo_lider, "serie": _serie_from_df(historial)},
        "totales": {
            "total_catalogo": len(catalogo),
            "titulos_activos": len(resumen),
            "pedidos_sugeridos": int((resumen["riesgo"] != "Bajo").sum()),
            "tirada_total": int(resumen["tiraje_recomendado"].sum()),
        },
    }


def list_catalogo(
    resultado: PipelineResult,
    q: str | None = None,
    page: int = 1,
    page_size: int = 20,
    riesgo: str | None = None,
) -> dict:
    catalogo = load_catalog()
    resumen = resultado.resumen_titulos.set_index("id_titulo")

    df = catalogo.copy()
    df["demanda_prevista"] = df["id_titulo"].map(resumen["demanda_prevista"])
    df["riesgo"] = df["id_titulo"].map(resumen["riesgo"])
    df["tiene_historial"] = df["id_titulo"].isin(resumen.index)

    if q:
        ql = q.lower()
        df = df[
            df["titulo_catalogo"].str.lower().str.contains(ql, na=False)
            | df["autor"].str.lower().str.contains(ql, na=False)
        ]
    if riesgo and riesgo != "Todas":
        df = df[df["riesgo"] == riesgo]

    total = len(df)
    total_pages = max(1, -(-total // page_size))
    inicio = (page - 1) * page_size
    pagina = df.iloc[inicio : inicio + page_size]

    items = [
        {
            "id_titulo": fila.id_titulo,
            "titulo": fila.titulo_catalogo,
            "autor": fila.autor,
            "genero": fila.genero,
            "demanda_prevista": _none_if_nan(fila.demanda_prevista),
            "riesgo": _none_if_nan(fila.riesgo),
            "tiene_historial": bool(fila.tiene_historial),
        }
        for fila in pagina.itertuples()
    ]
    return {"items": items, "page": page, "page_size": page_size, "total": total, "total_pages": total_pages}


def get_catalogo_detalle(resultado: PipelineResult, id_titulo: str) -> dict | None:
    catalogo = load_catalog().set_index("id_titulo")
    if id_titulo not in catalogo.index:
        return None
    fila_cat = catalogo.loc[id_titulo]

    resumen = resultado.resumen_titulos.set_index("id_titulo")
    tiene_historial = id_titulo in resumen.index

    base = {
        "id_titulo": id_titulo,
        "titulo": fila_cat.titulo_catalogo,
        "autor": fila_cat.autor,
        "genero": fila_cat.genero,
        "formato": _none_if_nan(fila_cat.formato),
        "n_paginas": _none_if_nan(fila_cat.n_paginas),
        "pvp": _none_if_nan(fila_cat.pvp),
        "tiene_historial": tiene_historial,
        "resumen": None,
        "historial": None,
        "factores": None,
        "recomendacion_texto": None,
    }
    if not tiene_historial:
        return base

    fila = resumen.loc[id_titulo]
    titulo_bd = fila["titulo"]

    historial = resultado.df_features[
        (resultado.df_features["titulo"] == titulo_bd) & resultado.df_features["ventas"].notna()
    ][["fecha", "ventas"]].sort_values("fecha")

    fila_features = resultado.df_features[
        (resultado.df_features["titulo"] == titulo_bd)
        & resultado.df_features[list(FEATURE_COLUMNS)].notna().all(axis=1)
        & resultado.df_features["ventas"].isna()
    ]
    factores = None
    if not fila_features.empty:
        importancia = compute_feature_importance(resultado.modelo_activo, fila_features[list(FEATURE_COLUMNS)])
        factores = importancia.to_dict(orient="records")

    base.update({
        "resumen": {
            "stock_actual_estimado": float(fila["stock_actual_estimado"]),
            "demanda_prevista": float(fila["demanda_prevista"]),
            "tiraje_recomendado": float(fila["tiraje_recomendado"]),
            "riesgo": fila["riesgo"],
            "confianza_modelo": float(fila["confianza_modelo"]),
        },
        "historial": _serie_from_df(historial),
        "factores": factores,
        "recomendacion_texto": (
            f"Se recomienda imprimir {fila['tiraje_recomendado']:,.0f} ejemplares para el próximo período."
        ),
    })
    return base


def orden_impresion_csv(resultado: PipelineResult, id_titulo: str) -> str | None:
    resumen = resultado.resumen_titulos.set_index("id_titulo")
    if id_titulo not in resumen.index:
        return None
    fila = resumen.loc[[id_titulo]]
    buffer = io.StringIO()
    fila.reset_index().to_csv(buffer, index=False)
    return buffer.getvalue()


def _mensaje_alerta(fila) -> tuple[str, str]:
    """Misma lógica if/elif que ya usaba app/pages/alertas.py en Streamlit,
    expuesta ahora como un campo estructurado (tipo_alerta) + texto."""
    delta_demanda = fila["demanda_prevista"] - fila["stock_actual_estimado"]
    if fila["riesgo"] == "Alto" and delta_demanda > 0:
        return "quiebre", (
            f"Riesgo de desabastecimiento: la demanda esperada "
            f"({fila['demanda_prevista']:,.0f}) supera el stock estimado "
            f"({fila['stock_actual_estimado']:,.0f})."
        )
    if fila["riesgo"] == "Alto":
        return "sobrestock", (
            f"Posible sobrestock: el stock estimado "
            f"({fila['stock_actual_estimado']:,.0f}) excede ampliamente "
            f"la demanda prevista ({fila['demanda_prevista']:,.0f})."
        )
    if fila["riesgo"] == "Medio":
        return "demanda_inusual", (
            f"Desviación moderada entre demanda prevista "
            f"({fila['demanda_prevista']:,.0f}) y stock estimado "
            f"({fila['stock_actual_estimado']:,.0f})."
        )
    return "normal", "Demanda y stock estimado dentro de los parámetros normales."


def get_alertas(resultado: PipelineResult, riesgo: str | None = None) -> dict:
    resumen = resultado.resumen_titulos
    conteos = {
        "Todas": len(resumen),
        "Alto": int((resumen["riesgo"] == "Alto").sum()),
        "Medio": int((resumen["riesgo"] == "Medio").sum()),
        "Bajo": int((resumen["riesgo"] == "Bajo").sum()),
    }

    vista = resumen if not riesgo or riesgo == "Todas" else resumen[resumen["riesgo"] == riesgo]
    orden = {"Alto": 0, "Medio": 1, "Bajo": 2}
    vista = vista.sort_values("riesgo", key=lambda s: s.map(orden))

    items = []
    for fila in vista.itertuples():
        tipo, mensaje = _mensaje_alerta(fila._asdict())
        items.append({
            "id_titulo": fila.id_titulo,
            "titulo": fila.titulo,
            "riesgo": fila.riesgo,
            "tipo_alerta": tipo,
            "demanda_prevista": float(fila.demanda_prevista),
            "stock_actual_estimado": float(fila.stock_actual_estimado),
            "tiraje_recomendado": float(fila.tiraje_recomendado),
            "mensaje": mensaje,
        })
    return {"conteos": conteos, "items": items}


def get_modelos(resultado: PipelineResult) -> dict:
    filas = [
        {
            "modelo": row["modelo"],
            "mape": row["mape"],
            "mae": row["mae"],
            "rmse": row["rmse"],
            "tiempo_entrenamiento_seg": row["tiempo_entrenamiento_seg"],
            "estado": "Activo" if row["modelo"] == resultado.modelo_ganador else "Disponible",
        }
        for row in resultado.comparacion_modelos.to_dict(orient="records")
    ]
    filas.append({
        "modelo": "LSTM",
        "mape": None,
        "mae": None,
        "rmse": None,
        "tiempo_entrenamiento_seg": None,
        "estado": "Próximamente",
    })
    return {"modelo_activo": resultado.modelo_ganador, "filas": filas}


def simulate_scenario(
    resultado: PipelineResult,
    id_titulo: str,
    ajuste_tendencia: int = 0,
    ajuste_estacionalidad: int = 0,
) -> dict | None:
    resumen = resultado.resumen_titulos.set_index("id_titulo")
    if id_titulo not in resumen.index:
        return None
    fila_resumen = resumen.loc[id_titulo]
    titulo_bd = fila_resumen["titulo"]

    fila_features = resultado.df_features[
        (resultado.df_features["titulo"] == titulo_bd)
        & resultado.df_features["ventas"].isna()
        & resultado.df_features[list(FEATURE_COLUMNS)].notna().all(axis=1)
    ]
    if fila_features.empty:
        return None

    X = fila_features[list(FEATURE_COLUMNS)].copy()
    columnas_tendencia = ["lag_1", "lag_2", "lag_3", "rolling_mean_3", "rolling_mean_6"]
    X[columnas_tendencia] = X[columnas_tendencia] * (1 + ajuste_tendencia / 100)

    demanda_base = resultado.modelo_activo.predict(X)[0]
    demanda_proyectada = float(demanda_base * (1 + ajuste_estacionalidad / 100))
    tiraje = float(recommend_print_run(np.array([demanda_proyectada]))[0])

    stock_actual = float(fila_resumen["stock_actual_estimado"])
    prob_quiebre = (
        max(0.0, min(100.0, (demanda_proyectada - stock_actual) / demanda_proyectada * 100))
        if demanda_proyectada > stock_actual
        else 0.0
    )
    prob_sobrestock = (
        max(0.0, min(100.0, (stock_actual - demanda_proyectada) / stock_actual * 100))
        if stock_actual > demanda_proyectada
        else 0.0
    )

    return {
        "demanda_proyectada": demanda_proyectada,
        "tiraje_recomendado": tiraje,
        "prob_quiebre": prob_quiebre,
        "prob_sobrestock": prob_sobrestock,
        "confianza_modelo": float(fila_resumen["confianza_modelo"]),
    }


def get_configuracion(resultado: PipelineResult) -> dict:
    return {
        "print_run_safety_buffer": config.PRINT_RUN_SAFETY_BUFFER,
        "risk_low_max_deviation": config.RISK_LOW_MAX_DEVIATION,
        "risk_medium_max_deviation": config.RISK_MEDIUM_MAX_DEVIATION,
        "test_months_per_title": config.TEST_MONTHS_PER_TITLE,
        "baseline_window_months": config.BASELINE_WINDOW_MONTHS,
        "model_version": config.MODEL_VERSION,
        "modelo_activo": resultado.modelo_ganador,
    }


def get_recomendaciones(resultado: PipelineResult) -> list[dict]:
    tabla = resultado.resumen_titulos[[
        "id_titulo", "titulo_catalogo", "autor", "genero", "demanda_prevista",
        "tiraje_recomendado", "stock_actual_estimado", "riesgo", "confianza_modelo",
    ]].rename(columns={"titulo_catalogo": "titulo"})
    return tabla.to_dict(orient="records")


def recomendaciones_csv(resultado: PipelineResult) -> str:
    buffer = io.StringIO()
    pd.DataFrame(get_recomendaciones(resultado)).to_csv(buffer, index=False)
    return buffer.getvalue()


def recomendaciones_xlsx(resultado: PipelineResult) -> bytes:
    buffer = io.BytesIO()
    pd.DataFrame(get_recomendaciones(resultado)).to_excel(buffer, index=False, engine="openpyxl")
    return buffer.getvalue()
