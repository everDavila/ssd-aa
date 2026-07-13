"""Carga y limpieza del dataset real de ventas (ficha_de_registro_v1.xlsx)."""

import pandas as pd

from ssd_aa.config import RAW_HEADER_ROW, RAW_SHEET_NAME, RAW_XLSX_PATH

_MONTH_MAP = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}


def _parse_periodo(periodo: str) -> pd.Timestamp:
    mes, anio = periodo.strip().lower().split("-")
    return pd.Timestamp(year=2000 + int(anio), month=_MONTH_MAP[mes], day=1)


def load_raw(path=RAW_XLSX_PATH) -> pd.DataFrame:
    """Lee la hoja BASE_DATOS. El encabezado real está en la fila 12 (las
    primeras 11 filas son metadatos de la ficha de registro académica)."""
    df = pd.read_excel(
        path, sheet_name=RAW_SHEET_NAME, header=RAW_HEADER_ROW - 1,
        usecols="A:D",
    )
    # Se renombra por posición (no por texto de encabezado): el Excel fuente
    # trae encabezados con acentos que difieren entre versiones de la ficha.
    df.columns = ["id_reg", "titulo", "periodo", "ventas"]
    df["fecha"] = df["periodo"].apply(_parse_periodo)
    return df[["id_reg", "titulo", "fecha", "ventas"]]


def aggregate_monthly(df_raw: pd.DataFrame) -> pd.DataFrame:
    """Suma los registros transaccionales a demanda mensual real por título.

    El Excel fuente trae hasta 6 filas para el mismo (título, mes): son ventas
    individuales, no la demanda mensual. Sin este paso, el mismo mes se cuenta
    varias veces y las features de series temporales quedan mal definidas.
    """
    monthly = (
        df_raw.groupby(["titulo", "fecha"], as_index=False)["ventas"]
        .sum()
        .sort_values(["titulo", "fecha"])
        .reset_index(drop=True)
    )
    return monthly
