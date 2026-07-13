"""Catálogo de títulos (autor, género, páginas, precio) desde
ficha-catalogo-mejorado.xlsx, reconciliado con los títulos que realmente
tienen historial de ventas en ficha_de_registro_v1.xlsx.

Se leen las hojas por posición (no por nombre): el Excel fuente usa guiones
largos en los nombres de hoja cuya codificación varía entre versiones.
"""

import pandas as pd

from ssd_aa.config import (
    CATALOG_HEADER_ROW,
    CATALOG_SHEET_INDEX,
    CATALOG_TIPO_A_OVERRIDES,
    CATALOG_TIPO_A_SHEET_INDEX,
    CATALOG_XLSX_PATH,
)

_CATALOG_COLUMNS = [
    "id_titulo", "nivel", "grado", "titulo_catalogo", "autor", "ilustrador",
    "lugar_origen", "formato", "papel", "encuadernacion", "n_paginas",
    "genero", "estado_stock", "pvp", "tiene_historial_catalogo", "tipo_registro_catalogo",
]


def load_catalog(path=CATALOG_XLSX_PATH) -> pd.DataFrame:
    """Catálogo completo (55 títulos, primaria + secundaria)."""
    df = pd.read_excel(
        path, sheet_name=CATALOG_SHEET_INDEX, header=CATALOG_HEADER_ROW - 1,
        usecols="A:P",
    )
    df.columns = _CATALOG_COLUMNS
    # La hoja trae 2 filas de leyenda al final (texto en la columna id_titulo,
    # no un TIT-XXX real); se filtran por patrón en vez de por nulos.
    df = df[df["id_titulo"].astype(str).str.match(r"^TIT-\d+$")]
    return df.reset_index(drop=True)


def load_titulo_bd_ventas_map(path=CATALOG_XLSX_PATH) -> dict:
    """Mapa id_titulo -> título tal como aparece en ficha_de_registro_v1.xlsx,
    a partir de la hoja 'TIPO A' (títulos con historial), con la corrección de
    CATALOG_TIPO_A_OVERRIDES para el título que el catálogo etiquetó mal."""
    df = pd.read_excel(
        path, sheet_name=CATALOG_TIPO_A_SHEET_INDEX, header=CATALOG_HEADER_ROW - 1,
        usecols="A:C",
    )
    df.columns = ["id_titulo", "titulo_catalogo", "titulo_bd_ventas"]
    df = df.dropna(subset=["id_titulo"])
    mapa = dict(zip(df["id_titulo"], df["titulo_bd_ventas"]))
    mapa.update(CATALOG_TIPO_A_OVERRIDES)
    return mapa


def catalog_by_titulo_bd_ventas(path=CATALOG_XLSX_PATH) -> pd.DataFrame:
    """Catálogo indexado por el nombre de título usado en la base de ventas
    (`titulo`), listo para unir con las predicciones del pipeline. Solo
    incluye los títulos que realmente tienen historial de ventas."""
    catalogo = load_catalog(path)
    mapa = load_titulo_bd_ventas_map(path)
    catalogo = catalogo[catalogo["id_titulo"].isin(mapa)].copy()
    catalogo["titulo"] = catalogo["id_titulo"].map(mapa)
    return catalogo.set_index("titulo")
