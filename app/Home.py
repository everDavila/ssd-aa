import streamlit as st

from ssd_aa.ui.auth import is_authenticated, render_login
from ssd_aa.ui.theme import inject_css

st.set_page_config(page_title="SSD Editorial", page_icon="📚", layout="wide")
inject_css()

if not is_authenticated():
    render_login()
    st.stop()

paginas = [
    st.Page("pages/dashboard.py", title="Dashboard", icon="🏠", default=True),
    st.Page("pages/catalogo.py", title="Catálogo de Libros", icon="📖"),
    st.Page("pages/predicciones.py", title="Predicciones", icon="📈"),
    st.Page("pages/alertas.py", title="Alertas", icon="🔔"),
    st.Page("pages/modelos_ia.py", title="Modelos IA", icon="🤖"),
    st.Page("pages/simulador.py", title="Simulador", icon="🎛️"),
    st.Page("pages/reportes_config.py", title="Reportes y Configuración", icon="⚙️"),
]

with st.sidebar:
    st.markdown("### 📚 SSD Editorial")
    st.caption("Campaña: Escolar 2026 · Planificador")

navegacion = st.navigation(paginas)
navegacion.run()

with st.sidebar:
    st.divider()
    if st.button("Cerrar sesión", width="stretch"):
        st.session_state["autenticado"] = False
        st.rerun()
