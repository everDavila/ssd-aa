"""Entrenamiento y selección de modelos (Regresión Lineal, Random Forest, XGBoost).

LSTM queda fuera de este MVP (requiere TensorFlow + ventanas de secuencia); en
la Tabla 12 de la propia tesis, XGBoost ya iguala o supera a LSTM en precisión
y es notablemente más rápido, así que no es una pérdida crítica para un
primer producto funcional.
"""

from datetime import datetime, timezone

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor

from ssd_aa.config import MODEL_VERSION, MODELS_DIR, TEST_MONTHS_PER_TITLE
from ssd_aa.features import FEATURE_COLUMNS
from ssd_aa.metrics import mae, mape, rmse


class LogTargetRegressor:
    """Envuelve un regresor para entrenarlo sobre log1p(ventas) en vez de
    ventas crudas. Las ventas por título abarcan dos órdenes de magnitud
    (10 a ~1,200 unidades/mes); sin esta transformación, los títulos de bajo
    volumen dominan el error porcentual y el modelo termina sin superar a la
    media móvil simple. `predict` siempre devuelve unidades reales.
    """

    def __init__(self, base_estimator):
        self.base_estimator = base_estimator

    def fit(self, X, y):
        self.base_estimator.fit(X, np.log1p(y))
        return self

    def predict(self, X):
        return np.expm1(self.base_estimator.predict(X))


MODEL_FACTORIES = {
    "Regresión Lineal": lambda: LogTargetRegressor(LinearRegression()),
    "Random Forest": lambda: LogTargetRegressor(
        RandomForestRegressor(n_estimators=300, max_depth=8, random_state=42)
    ),
    "XGBoost": lambda: LogTargetRegressor(XGBRegressor(
        n_estimators=300, max_depth=4, learning_rate=0.05, random_state=42,
    )),
}


def time_based_split(df: pd.DataFrame, test_months: int = TEST_MONTHS_PER_TITLE):
    """Separa train/test por título usando los últimos `test_months` meses de
    cada título como test (sin fuga temporal: nunca se entrena con el futuro)."""
    df = df.sort_values(["titulo", "fecha"])
    es_test = df.groupby("titulo")["fecha"].rank(method="first", ascending=False) <= test_months
    return df.loc[~es_test].reset_index(drop=True), df.loc[es_test].reset_index(drop=True)


def train_and_compare(df_train: pd.DataFrame, df_test: pd.DataFrame) -> dict:
    """Entrena los 3 modelos y devuelve sus métricas + los objetos entrenados."""
    X_train, y_train = df_train[FEATURE_COLUMNS], df_train["ventas"]
    X_test, y_test = df_test[FEATURE_COLUMNS], df_test["ventas"]

    resultados = {}
    for nombre, fabrica in MODEL_FACTORIES.items():
        modelo = fabrica()
        inicio = datetime.now(timezone.utc)
        modelo.fit(X_train, y_train)
        duracion = (datetime.now(timezone.utc) - inicio).total_seconds()
        predicho = modelo.predict(X_test)
        resultados[nombre] = {
            "modelo": modelo,
            "mae": mae(y_test, predicho),
            "rmse": rmse(y_test, predicho),
            "mape": mape(y_test, predicho),
            "tiempo_entrenamiento_seg": duracion,
        }
    return resultados


def select_winner(resultados: dict) -> str:
    return min(resultados, key=lambda nombre: resultados[nombre]["mape"])


def save_winner(nombre: str, resultados: dict, feature_columns=FEATURE_COLUMNS) -> None:
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(resultados[nombre]["modelo"], MODELS_DIR / "modelo_activo.joblib")
    metadata = {
        "nombre_modelo": nombre,
        "version": MODEL_VERSION,
        "entrenado_en": datetime.now(timezone.utc).isoformat(),
        "feature_columns": list(feature_columns),
        "mape_test": resultados[nombre]["mape"],
    }
    joblib.dump(metadata, MODELS_DIR / "metadata.joblib")


def load_winner():
    modelo = joblib.load(MODELS_DIR / "modelo_activo.joblib")
    metadata = joblib.load(MODELS_DIR / "metadata.joblib")
    return modelo, metadata
