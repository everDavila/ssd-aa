import streamlit as st

from ssd_aa.ui.book_detail import render_book_detail
from ssd_aa.ui.state import get_pipeline_result

st.markdown("### 📈 Predicciones")

resultado = get_pipeline_result()
titulos = sorted(resultado.resumen_titulos["titulo"].unique())
titulo = st.selectbox("Selecciona un título", titulos)

st.divider()
render_book_detail(resultado, titulo)
