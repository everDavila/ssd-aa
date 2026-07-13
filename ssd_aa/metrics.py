"""Métricas de error y de gestión de inventario (D1-D3 de la tesis), calculadas
sobre datos reales en vez de copiadas de la investigación."""

import numpy as np
import pandas as pd

from ssd_aa.config import PRINT_RUN_SAFETY_BUFFER

_EPS = 1e-9


def mae(actual: pd.Series, predicho: pd.Series) -> float:
    return float(np.mean(np.abs(actual - predicho)))


def rmse(actual: pd.Series, predicho: pd.Series) -> float:
    return float(np.sqrt(np.mean((actual - predicho) ** 2)))


def mape(actual: pd.Series, predicho: pd.Series) -> float:
    actual = np.asarray(actual, dtype=float)
    predicho = np.asarray(predicho, dtype=float)
    denominador = np.maximum(np.abs(actual), _EPS)
    return float(np.mean(np.abs(actual - predicho) / denominador) * 100)


def recommend_print_run(forecast: pd.Series, buffer: float = PRINT_RUN_SAFETY_BUFFER) -> pd.Series:
    """Tiraje recomendado = pronóstico + colchón de seguridad, redondeado hacia
    arriba (no se pueden imprimir fracciones de ejemplar).

    Se redondea a 6 decimales antes de `ceil` para evitar que la imprecisión
    de punto flotante (p. ej. 100*1.1 = 110.00000000000001) infle el tiraje
    en una unidad cuando el resultado matemático es un entero exacto.
    """
    return np.ceil(np.round(np.asarray(forecast, dtype=float) * (1 + buffer), 6))


def overstock_pct(actual: pd.Series, tiraje: pd.Series) -> float:
    """Promedio del exceso de inventario cuando el tiraje superó la venta real,
    expresado como % del propio tiraje (D2)."""
    tiraje = np.asarray(tiraje, dtype=float)
    actual = np.asarray(actual, dtype=float)
    exceso = np.clip(tiraje - actual, a_min=0, a_max=None)
    ratio = exceso / np.maximum(tiraje, _EPS)
    return float(np.mean(ratio) * 100)


def stockout_pct(actual: pd.Series, tiraje: pd.Series) -> float:
    """Promedio del faltante cuando la venta real superó el tiraje, expresado
    como % de la propia venta real (D3)."""
    tiraje = np.asarray(tiraje, dtype=float)
    actual = np.asarray(actual, dtype=float)
    faltante = np.clip(actual - tiraje, a_min=0, a_max=None)
    ratio = faltante / np.maximum(actual, _EPS)
    return float(np.mean(ratio) * 100)


def risk_level(demanda_prevista: float, referencia: float, umbral_bajo: float, umbral_medio: float) -> str:
    """Clasifica el riesgo de un título comparando la demanda prevista contra
    una referencia (tiraje del período anterior o stock disponible)."""
    if referencia <= 0:
        return "Alto" if demanda_prevista > 0 else "Bajo"
    desviacion = abs(demanda_prevista - referencia) / referencia
    if desviacion <= umbral_bajo:
        return "Bajo"
    if desviacion <= umbral_medio:
        return "Medio"
    return "Alto"
