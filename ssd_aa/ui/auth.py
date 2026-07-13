"""Gate de sesión de un solo usuario (sin base de datos de usuarios): adecuado
para el despliegue local de una sola Pyme editorial que ya describen la tesis
y el capstone. No es autenticación multiusuario real."""

import streamlit as st
from streamlit.runtime.secrets import StreamlitSecretNotFoundError

_DEFAULT_CREDENCIALES = {"usuario": "editor", "contrasena": "ambar2026"}


def _credenciales() -> dict:
    """`st.secrets` lanza StreamlitSecretNotFoundError (no devuelve un dict
    vacío) cuando no existe ningún secrets.toml — que es la situación normal
    en este MVP mientras no se cree el archivo opcional."""
    try:
        return st.secrets["credenciales"]
    except (StreamlitSecretNotFoundError, KeyError):
        return _DEFAULT_CREDENCIALES


def is_authenticated() -> bool:
    return bool(st.session_state.get("autenticado"))


def render_login() -> None:
    st.markdown(
        "<h2 style='text-align:center;'>📚 SSD Editorial</h2>"
        "<p style='text-align:center;color:#6B7280;'>"
        "Sistema de Soporte a Decisiones — Predicción de Demanda Bibliográfica</p>",
        unsafe_allow_html=True,
    )
    _, centro, _ = st.columns([1, 1.2, 1])
    with centro:
        with st.form("login_form"):
            usuario = st.text_input("Usuario")
            contrasena = st.text_input("Contraseña", type="password")
            enviado = st.form_submit_button("Iniciar sesión", width="stretch")

        if enviado:
            credenciales = _credenciales()
            if usuario == credenciales["usuario"] and contrasena == credenciales["contrasena"]:
                st.session_state["autenticado"] = True
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos.")
        st.caption("Demo MVP — usuario: editor · contraseña: ambar2026")
