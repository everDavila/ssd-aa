from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
RAW_XLSX_PATH = ROOT_DIR / "input_locales" / "ficha_de_registro_v1.xlsx"
CATALOG_XLSX_PATH = ROOT_DIR / "input_locales" / "ficha-catalogo-mejorado.xlsx"
MODELS_DIR = ROOT_DIR / "models"

RAW_SHEET_NAME = "BASE_DATOS"
RAW_HEADER_ROW = 12  # 1-indexed: fila real de encabezados (ID_Reg, Titulo, Periodo, Ventas)

TITULOS_SHEET_NAME = "COD_TITULOS"

# Hojas del catálogo referenciadas por posición: el archivo fuente usa guiones
# largos en los nombres de hoja que varían de codificación entre versiones.
CATALOG_SHEET_INDEX = 0  # "CATÁLOGO COMPLETO"
CATALOG_TIPO_A_SHEET_INDEX = 1  # "TIPO A — Con Historial ML" (mapa Título Catálogo -> Título BD Ventas)
CATALOG_HEADER_ROW = 3  # 1-indexed

# El propio archivo de catálogo marca TIT-010 "Beto, el espantapájaros" como
# TIPO B (sin historial), pero ese título SÍ tiene 54 registros reales en
# ficha_de_registro_v1.xlsx. Se corrige aquí en vez de en el Excel fuente.
CATALOG_TIPO_A_OVERRIDES = {
    "TIT-010": "Beto el Espantapájaros",
}

# Meses más recientes por título reservados para test (split temporal, no aleatorio).
TEST_MONTHS_PER_TITLE = 6

# Meses usados por el baseline "método empírico" (media móvil).
BASELINE_WINDOW_MONTHS = 3

# Colchón de seguridad aplicado sobre el pronóstico para sugerir el tiraje a imprimir.
PRINT_RUN_SAFETY_BUFFER = 0.15

# Umbrales de riesgo (ratio demanda_prevista / tiraje_recomendado_anterior) para
# clasificar cada título como riesgo bajo/medio/alto en el dashboard y alertas.
RISK_LOW_MAX_DEVIATION = 0.10
RISK_MEDIUM_MAX_DEVIATION = 0.25

MODEL_VERSION = "v1.0"
