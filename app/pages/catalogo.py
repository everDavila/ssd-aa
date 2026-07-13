import pandas as pd
import streamlit as st

from ssd_aa.catalog import load_catalog
from ssd_aa.ui.book_detail import render_book_detail
from ssd_aa.ui.components import risk_label_with_emoji
from ssd_aa.ui.state import get_pipeline_result

st.markdown("### 📖 Catálogo de Libros")

resultado = get_pipeline_result()
catalogo = load_catalog()
resumen = resultado.resumen_titulos.set_index("id_titulo")

busqueda = st.text_input("Buscar por título o autor", "")

vista = catalogo.copy()
if busqueda:
    filtro = busqueda.lower()
    vista = vista[
        vista["titulo_catalogo"].str.lower().str.contains(filtro)
        | vista["autor"].str.lower().str.contains(filtro)
    ]

vista["Demanda Prevista"] = vista["id_titulo"].map(resumen["demanda_prevista"])
vista["Riesgo"] = vista["id_titulo"].map(resumen["riesgo"]).fillna("Sin historial")
vista["Riesgo"] = vista["Riesgo"].map(lambda r: risk_label_with_emoji(r) if r != "Sin historial" else "⚪ Sin historial")
vista["Demanda Prevista"] = vista["Demanda Prevista"].map(lambda v: f"{v:,.0f}" if pd.notna(v) else "—")

tabla = vista.rename(columns={
    "titulo_catalogo": "Título", "autor": "Autor", "genero": "Categoría",
}).sort_values("Título")

evento = st.dataframe(
    tabla[["id_titulo", "Título", "Autor", "Categoría", "Demanda Prevista", "Riesgo"]],
    hide_index=True, width="stretch",
    on_select="rerun", selection_mode="single-row", key="tabla_catalogo",
)

st.caption(f"{len(tabla)} títulos · {resumen.shape[0]} con historial de ventas para pronóstico ML")

filas_seleccionadas = evento.selection.rows if evento and evento.selection else []
if filas_seleccionadas:
    id_titulo = tabla.iloc[filas_seleccionadas[0]]["id_titulo"]
    if id_titulo in resumen.index:
        titulo_bd = resumen.loc[id_titulo, "titulo"]
        st.divider()
        render_book_detail(resultado, titulo_bd)
    else:
        st.divider()
        st.info(
            f"**{tabla.iloc[filas_seleccionadas[0]]['Título']}** no tiene historial de ventas "
            "todavía, por lo que no participa del pronóstico ML (ver catálogo: "
            "'Acción Requerida: Recolectar ventas históricas 2022–2025')."
        )
