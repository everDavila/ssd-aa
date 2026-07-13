import pandas as pd

from ssd_aa.data import aggregate_monthly, load_raw


def test_load_raw_has_expected_shape_and_columns():
    df = load_raw()
    assert list(df.columns) == ["id_reg", "titulo", "fecha", "ventas"]
    assert len(df) == 1280
    assert df["titulo"].nunique() == 21


def test_aggregate_monthly_sums_duplicate_titulo_periodo():
    """El Excel fuente trae hasta 6 filas para el mismo (título, mes): deben
    sumarse, no promediarse ni quedarse con la primera."""
    df_raw = pd.DataFrame({
        "id_reg": [1, 2, 3],
        "titulo": ["A", "A", "B"],
        "fecha": [pd.Timestamp("2023-01-01")] * 2 + [pd.Timestamp("2023-01-01")],
        "ventas": [10, 5, 7],
    })
    mensual = aggregate_monthly(df_raw)
    assert len(mensual) == 2
    fila_a = mensual[mensual["titulo"] == "A"].iloc[0]
    assert fila_a["ventas"] == 15


def test_aggregate_monthly_real_dataset_has_no_duplicate_titulo_fecha():
    mensual = aggregate_monthly(load_raw())
    assert not mensual.duplicated(subset=["titulo", "fecha"]).any()
