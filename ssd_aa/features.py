"""Features de series temporales por título a partir de la demanda mensual agregada."""

import numpy as np
import pandas as pd

LAGS = (1, 2, 3)
ROLLING_WINDOWS = (3, 6)


def _reindex_calendar(monthly: pd.DataFrame) -> pd.DataFrame:
    """Reexpresa cada título sobre el calendario mensual completo del dataset,
    dejando NaN en 'ventas' para los meses sin registro (falta de reporte, no
    venta cero) — así los lags reflejan meses calendario reales, no posiciones.

    Se agrega un mes extra al final (más allá del último dato real) para que
    cada título tenga, tras calcular lags, exactamente una fila 'siguiente
    mes' con features completas pero ventas desconocida: es la fila que se
    usa para el pronóstico a futuro (ver `pipeline.forecast_next_month`).
    """
    fin = monthly["fecha"].max() + pd.DateOffset(months=1)
    calendario = pd.date_range(monthly["fecha"].min(), fin, freq="MS")
    piezas = []
    for titulo, grupo in monthly.groupby("titulo"):
        serie = grupo.set_index("fecha")["ventas"].reindex(calendario)
        piezas.append(pd.DataFrame({"titulo": titulo, "fecha": calendario, "ventas": serie.values}))
    return pd.concat(piezas, ignore_index=True)


def build_features(monthly: pd.DataFrame) -> pd.DataFrame:
    """Genera lags, medias móviles y estacionalidad por título sobre el
    calendario mensual completo (ver `_reindex_calendar`)."""
    df = _reindex_calendar(monthly).sort_values(["titulo", "fecha"]).reset_index(drop=True)

    for lag in LAGS:
        df[f"lag_{lag}"] = df.groupby("titulo")["ventas"].shift(lag)

    for window in ROLLING_WINDOWS:
        df[f"rolling_mean_{window}"] = (
            df.groupby("titulo")["ventas"]
            .shift(1)
            .rolling(window=window, min_periods=1)
            .mean()
            .reset_index(level=0, drop=True)
        )

    df["mes"] = df["fecha"].dt.month
    df["mes_seno"] = np.sin(2 * np.pi * df["mes"] / 12)
    df["mes_coseno"] = np.cos(2 * np.pi * df["mes"] / 12)
    df["titulo_cod"] = df["titulo"].astype("category").cat.codes

    return df


FEATURE_COLUMNS = (
    [f"lag_{lag}" for lag in LAGS]
    + [f"rolling_mean_{w}" for w in ROLLING_WINDOWS]
    + ["mes_seno", "mes_coseno", "titulo_cod"]
)


def rows_with_full_history(df_features: pd.DataFrame) -> pd.DataFrame:
    """Filas con target real (mes sí reportado) y todos los lags/rolling
    disponibles (sin NaN), listas para entrenar o evaluar."""
    return df_features.dropna(subset=["ventas", *FEATURE_COLUMNS]).reset_index(drop=True)
