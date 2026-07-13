import numpy as np
import pytest

from ssd_aa.metrics import mae, mape, overstock_pct, recommend_print_run, risk_level, rmse, stockout_pct


def test_mape_known_vectors():
    actual = np.array([100, 200, 50])
    predicho = np.array([110, 180, 50])
    # errores relativos: 10/100, 20/200, 0/50 -> 10%, 10%, 0% -> media 6.666...%
    assert mape(actual, predicho) == pytest.approx(6.6667, abs=1e-3)


def test_mae_and_rmse_known_vectors():
    actual = np.array([10, 20, 30])
    predicho = np.array([12, 18, 33])
    assert mae(actual, predicho) == pytest.approx(np.mean([2, 2, 3]))
    assert rmse(actual, predicho) == pytest.approx(np.sqrt(np.mean([4, 4, 9])))


def test_recommend_print_run_applies_buffer_and_rounds_up():
    tiraje = recommend_print_run(np.array([100, 101]), buffer=0.1)
    assert list(tiraje) == [110, 112]  # ceil(100*1.1)=110, ceil(101*1.1)=112 (111.1 -> 112)


def test_overstock_pct_only_counts_excess_inventory():
    actual = np.array([80, 120])
    tiraje = np.array([100, 100])  # título 1: sobrestock de 20/100; título 2: quiebre (no cuenta aquí)
    assert overstock_pct(actual, tiraje) == pytest.approx(10.0)  # media de [20%, 0%]


def test_stockout_pct_only_counts_unmet_demand():
    actual = np.array([80, 120])
    tiraje = np.array([100, 100])  # título 1: no hay quiebre; título 2: faltan 20/120
    assert stockout_pct(actual, tiraje) == pytest.approx(np.mean([0, 20 / 120 * 100]))


def test_risk_level_thresholds():
    assert risk_level(100, 100, umbral_bajo=0.10, umbral_medio=0.25) == "Bajo"
    assert risk_level(120, 100, umbral_bajo=0.10, umbral_medio=0.25) == "Medio"
    assert risk_level(150, 100, umbral_bajo=0.10, umbral_medio=0.25) == "Alto"
