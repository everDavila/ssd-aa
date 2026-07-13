"""Pruebas unitarias del pipeline completo (PU01-PU05), sobre datos reales."""

import numpy as np
import pandas as pd
import pytest

from ssd_aa.data import load_raw, aggregate_monthly
from ssd_aa.features import build_features, rows_with_full_history, FEATURE_COLUMNS
from ssd_aa.metrics import mape
from ssd_aa.pipeline import run_pipeline


def test_pu01_carga_historico_dimensiones():
    """PU01: la carga del archivo histórico devuelve los registros y columnas esperados."""
    df = load_raw()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1280
    assert list(df.columns) == ["id_reg", "titulo", "fecha", "ventas"]


def test_pu02_consolidacion_de_duplicados_titulo_periodo():
    """PU02: registros repetidos (mismo título + mes) se consolidan sumando las ventas."""
    df_raw = pd.DataFrame({
        "id_reg": [1, 2, 3],
        "titulo": ["A", "A", "B"],
        "fecha": [pd.Timestamp("2024-01-01")] * 2 + [pd.Timestamp("2024-01-01")],
        "ventas": [100, 100, 250],
    })
    resultado = aggregate_monthly(df_raw)
    assert len(resultado) == 2
    fila_a = resultado[resultado["titulo"] == "A"].iloc[0]
    assert fila_a["ventas"] == 200


def test_pu03_features_sin_nulos_tras_filtrar_historial_completo():
    """PU03: tras filtrar filas con historial completo, no deben quedar nulos
    en la venta ni en ninguna de las features usadas para entrenar/predecir."""
    mensual = aggregate_monthly(load_raw())
    df_features = build_features(mensual)
    df_hist = rows_with_full_history(df_features)
    assert len(df_hist) > 0
    assert df_hist[["ventas", *FEATURE_COLUMNS]].isna().sum().sum() == 0


def test_pu04_calculo_de_mape():
    """PU04: el MAPE coincide con el cálculo manual de referencia."""
    y_real = np.array([100.0, 200.0, 400.0])
    y_pred = np.array([110.0, 180.0, 440.0])
    # errores: 10%, 10%, 10% -> MAPE esperado = 10.0
    assert mape(y_real, y_pred) == pytest.approx(10.0, abs=1e-6)


def test_pu04b_mape_protege_division_por_cero():
    """PU04-b: el MAPE no debe romperse ante ventas iguales a cero."""
    y_real = np.array([0.0, 100.0])
    y_pred = np.array([5.0, 110.0])
    resultado = mape(y_real, y_pred)
    assert np.isfinite(resultado)


def test_pu05_pipeline_completo_prediccion_valida():
    """PU05: el pipeline completo entrena, elige un modelo ganador y produce,
    para cada título, una demanda prevista finita y no negativa."""
    resultado = run_pipeline()

    assert resultado.modelo_ganador in resultado.modelos
    assert np.isfinite(resultado.metricas_post["mape"])

    demanda_prevista = resultado.resumen_titulos["demanda_prevista"]
    assert len(demanda_prevista) > 0
    assert np.isfinite(demanda_prevista).all()
    assert (demanda_prevista >= 0).all()
