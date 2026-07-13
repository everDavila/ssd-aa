import streamlit as st

from ssd_aa.catalog import load_catalog
from ssd_aa.ui.components import forecast_chart, kpi_card, risk_label_with_emoji
from ssd_aa.ui.state import get_pipeline_result

st.markdown("### 🏠 Dashboard Ejecutivo")
st.caption(
    "Cifras calculadas en vivo sobre datos reales (2022–2025). El método "
    "'PRE' es una media móvil de 3 meses (proxy del criterio empírico del "
    "editor); no existe en los datos una columna con el tiraje que realmente "
    "se decidió en el pasado."
)

resultado = get_pipeline_result()
pre, post = resultado.metricas_pre, resultado.metricas_post
resumen = resultado.resumen_titulos

col1, col2, col3, col4 = st.columns(4)
with col1:
    kpi_card("MAPE actual", f"{post['mape']:.2f}%", f"{post['mape'] - pre['mape']:+.2f} pp vs. método tradicional")
with col2:
    kpi_card(
        "Sobrestock", f"{post['sobrestock_pct']:.2f}%",
        f"{post['sobrestock_pct'] - pre['sobrestock_pct']:+.2f} pp vs. método tradicional",
    )
with col3:
    kpi_card(
        "Quiebre de stock", f"{post['quiebre_pct']:.2f}%",
        f"{post['quiebre_pct'] - pre['quiebre_pct']:+.2f} pp vs. método tradicional",
        delta_color="inverse",
    )
with col4:
    kpi_card("Tiempo de proceso", f"{resultado.tiempo_total_seg:.2f} s", "Pipeline completo (carga a pronóstico)")

st.markdown("")
col_chart, col_riesgo = st.columns([2, 1])

with col_chart:
    titulo_muestra = resumen.sort_values("demanda_prevista", ascending=False)["titulo"].iloc[0]
    historial = resultado.df_test[resultado.df_test["titulo"] == titulo_muestra][["fecha", "ventas"]]
    st.plotly_chart(forecast_chart(historial, titulo_muestra), width="stretch")
    st.caption(
        "Se muestra el título con mayor demanda prevista. Este MVP pronostica "
        "un mes hacia adelante (no 6, como en el mockup original) dado el "
        "horizonte real de datos disponible por título."
    )

with col_riesgo:
    st.markdown("**Libros con mayor riesgo**")
    top_riesgo = resumen.sort_values("demanda_prevista", ascending=False).head(6).copy()
    top_riesgo["Riesgo"] = top_riesgo["riesgo"].map(risk_label_with_emoji)
    st.dataframe(
        top_riesgo[["titulo", "demanda_prevista", "Riesgo"]].rename(
            columns={"titulo": "Título", "demanda_prevista": "Demanda prevista"}
        ),
        hide_index=True, width="stretch",
    )

st.markdown("")
total_catalogo = len(load_catalog())
titulos_activos = len(resumen)
pedidos_sugeridos = int((resumen["riesgo"] != "Bajo").sum())
tirada_total = int(resumen["tiraje_recomendado"].sum())

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total de títulos (catálogo)", total_catalogo)
c2.metric("Títulos con pronóstico ML", titulos_activos)
c3.metric("Pedidos sugeridos (riesgo medio/alto)", pedidos_sugeridos)
c4.metric("Tirada recomendada total", f"{tirada_total:,}")
