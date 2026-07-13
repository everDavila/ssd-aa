"""Método 'empírico' (PRE): lo que un editor sin sistema estimaría a mano.

Se modela como la media móvil de los últimos BASELINE_WINDOW_MONTHS meses
reales del título — no existe en el dataset una columna con el tiraje que el
editor decidió históricamente, así que esta es la heurística más simple y
defendible para reconstruir el escenario PRE con datos reales.
"""

import pandas as pd

from ssd_aa.config import BASELINE_WINDOW_MONTHS


def forecast_naive(df_features: pd.DataFrame) -> pd.Series:
    columna = f"rolling_mean_{BASELINE_WINDOW_MONTHS}"
    if columna not in df_features.columns:
        raise ValueError(
            f"Falta la columna '{columna}'; BASELINE_WINDOW_MONTHS debe "
            "coincidir con una de las ventanas en features.ROLLING_WINDOWS."
        )
    return df_features[columna]
