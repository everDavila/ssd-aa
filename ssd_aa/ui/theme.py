"""Tema visual (morado/índigo, tarjetas redondeadas) que aproxima el look de
los mockups ya sustentados (input_locales/prototipos)."""

import streamlit as st

PRIMARY = "#6C4FF2"
PRIMARY_DARK = "#4C2FD1"
BG_APP = "#F5F3FE"
CARD_BG = "#FFFFFF"

RISK_COLORS = {
    "Bajo": ("#DCFCE7", "#15803D"),
    "Medio": ("#FEF3C7", "#B45309"),
    "Alto": ("#FEE2E2", "#B91C1C"),
}

_CSS = f"""
<style>
.stApp {{ background-color: {BG_APP}; }}
section[data-testid="stSidebar"] {{
    background-color: #241C4E;
}}
section[data-testid="stSidebar"] * {{ color: #E9E6FB !important; }}

div[data-testid="stMetric"] {{
    background-color: {CARD_BG};
    border-radius: 14px;
    padding: 1rem 1.2rem;
    box-shadow: 0 1px 3px rgba(76, 47, 209, 0.12);
}}

.ssd-card {{
    background-color: {CARD_BG};
    border-radius: 14px;
    padding: 1.1rem 1.3rem;
    box-shadow: 0 1px 3px rgba(76, 47, 209, 0.12);
    margin-bottom: 0.8rem;
}}

.ssd-badge {{
    display: inline-block;
    padding: 0.15rem 0.7rem;
    border-radius: 999px;
    font-weight: 600;
    font-size: 0.85rem;
}}

.stButton > button[kind="primary"], .stFormSubmitButton > button {{
    background-color: {PRIMARY};
    border-color: {PRIMARY};
}}
.stButton > button[kind="primary"]:hover, .stFormSubmitButton > button:hover {{
    background-color: {PRIMARY_DARK};
    border-color: {PRIMARY_DARK};
}}
</style>
"""


def inject_css() -> None:
    st.markdown(_CSS, unsafe_allow_html=True)


def risk_badge_html(nivel: str) -> str:
    bg, fg = RISK_COLORS.get(nivel, ("#E5E7EB", "#374151"))
    return f'<span class="ssd-badge" style="background-color:{bg};color:{fg};">{nivel}</span>'
