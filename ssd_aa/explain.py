"""Explicabilidad del modelo activo para la pantalla 'Factores que influyen'.

Los nombres de las palancas del mockup (campaña escolar, publicidad, precio,
competencia) no existen como columnas en el dataset real; aquí se explican
las features que el modelo sí usa (lags, medias móviles, estacionalidad,
título), con etiquetas en español legibles para un usuario no técnico.
"""

import numpy as np
import pandas as pd
import shap
from sklearn.linear_model import LinearRegression

from ssd_aa.features import FEATURE_COLUMNS

FEATURE_LABELS = {
    "lag_1": "Ventas del mes anterior",
    "lag_2": "Ventas de hace 2 meses",
    "lag_3": "Ventas de hace 3 meses",
    "rolling_mean_3": "Tendencia reciente (prom. 3 meses)",
    "rolling_mean_6": "Tendencia reciente (prom. 6 meses)",
    "mes_seno": "Estacionalidad del mes",
    "mes_coseno": "Estacionalidad del mes",
    "titulo_cod": "Perfil propio del título",
}


def compute_feature_importance(modelo, X: pd.DataFrame) -> pd.DataFrame:
    """Importancia promedio (valor absoluto de SHAP) por feature, agregando
    'mes_seno'/'mes_coseno' en un único factor 'Estacionalidad del mes'.

    SHAP se calcula en el espacio log1p en que entrena el modelo (ver
    `models.LogTargetRegressor`): los valores representan contribución
    relativa (multiplicativa) a la demanda, coherente con las barras en %
    del mockup 'Factores que influyen'.
    """
    base_estimator = getattr(modelo, "base_estimator", modelo)
    if isinstance(base_estimator, LinearRegression):
        base = X.mean()
        contrib = (X - base) * base_estimator.coef_
        shap_values = contrib.to_numpy()
    else:
        explainer = shap.TreeExplainer(base_estimator)
        shap_values = explainer.shap_values(X)

    promedio = pd.Series(np.mean(shap_values, axis=0), index=FEATURE_COLUMNS)
    etiquetas = promedio.rename(index=FEATURE_LABELS)
    agregado = etiquetas.groupby(level=0).sum().sort_values(key=np.abs, ascending=False)
    return agregado.rename("impacto").reset_index().rename(columns={"index": "factor"})
