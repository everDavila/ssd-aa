"""Componentes de UI reutilizados entre Dashboard/Catálogo/Detalle/Predicciones/Alertas."""

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from ssd_aa.ui.theme import risk_badge_html

RISK_EMOJI = {"Bajo": "🟢", "Medio": "🟡", "Alto": "🔴"}


def risk_label_with_emoji(nivel: str) -> str:
    return f"{RISK_EMOJI.get(nivel, '⚪')} {nivel}"


def risk_badge(nivel: str) -> None:
    st.markdown(risk_badge_html(nivel), unsafe_allow_html=True)


def kpi_card(label: str, value: str, delta: str | None = None, delta_color: str = "normal") -> None:
    st.metric(label, value, delta=delta, delta_color=delta_color)


def forecast_chart(historial: pd.DataFrame, titulo: str) -> go.Figure:
    """Línea de ventas reales + punto de pronóstico del próximo mes, similar
    al gráfico 'Ventas históricas y predicción' del mockup (pantalla 5)."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=historial["fecha"], y=historial["ventas"], mode="lines+markers",
        name="Ventas reales", line=dict(color="#6C4FF2", width=2),
    ))
    fig.update_layout(
        title=f"Demanda histórica — {titulo}",
        margin=dict(l=10, r=10, t=40, b=10),
        height=340,
        plot_bgcolor="white",
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )
    return fig


def shap_bar_chart(df_importancia: pd.DataFrame) -> go.Figure:
    """Barras horizontales de impacto por factor (mockup pantalla 6)."""
    df = df_importancia.sort_values("impacto")
    colores = ["#DC2626" if v < 0 else "#6C4FF2" for v in df["impacto"]]
    fig = go.Figure(go.Bar(
        x=df["impacto"], y=df["factor"], orientation="h",
        marker_color=colores,
    ))
    fig.update_layout(
        title="Factores que más influyen en la predicción",
        margin=dict(l=10, r=10, t=40, b=10),
        height=320,
        plot_bgcolor="white",
        xaxis_title="Impacto relativo (escala log)",
    )
    return fig


def model_comparison_chart(df_comparacion: pd.DataFrame) -> go.Figure:
    fig = go.Figure(go.Bar(
        x=df_comparacion["modelo"], y=df_comparacion["mape"],
        marker_color="#6C4FF2", text=df_comparacion["mape"].round(2), textposition="outside",
    ))
    fig.update_layout(
        title="MAPE por modelo (menor es mejor)",
        margin=dict(l=10, r=10, t=40, b=10), height=320, plot_bgcolor="white",
        yaxis_title="MAPE (%)",
    )
    return fig
