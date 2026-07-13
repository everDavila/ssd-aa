import pandas as pd
import pytest

from ssd_aa.baseline import forecast_naive
from ssd_aa.features import build_features


def test_forecast_naive_is_moving_average_of_last_3_real_months():
    monthly = pd.DataFrame({
        "titulo": ["A"] * 5,
        "fecha": pd.date_range("2023-01-01", periods=5, freq="MS"),
        "ventas": [10, 20, 30, 40, 50],
    })
    features = build_features(monthly)
    baseline = forecast_naive(features)

    fila_mayo = features[features["fecha"] == "2023-05-01"].index[0]
    # pronóstico de mayo = media de (feb, mar, abr) = media(20,30,40) = 30
    assert baseline.loc[fila_mayo] == pytest.approx(30.0)


def test_forecast_naive_raises_if_window_column_missing():
    df_sin_columna = pd.DataFrame({"ventas": [1, 2, 3]})
    with pytest.raises(ValueError):
        forecast_naive(df_sin_columna)
