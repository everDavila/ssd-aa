import numpy as np
import streamlit as st

from ssd_aa.features import FEATURE_COLUMNS
from ssd_aa.metrics import recommend_print_run
from ssd_aa.ui.state import get_pipeline_result

st.markdown("### 🎛️ Simulador de Escenarios")
st.caption(
    "El mockup original usaba variables ilustrativas (campaña escolar, "
    "publicidad, precio, competencia) que no existen en los datos reales. "
    "Este simulador ajusta las palancas que el modelo sí controla: la "
    "tendencia reciente de ventas y un factor de estacionalidad aplicado "
    "sobre el pronóstico."
)

resultado = get_pipeline_result()
resumen = resultado.resumen_titulos.set_index("titulo")
titulo = st.selectbox("Selecciona un título", sorted(resumen.index))

col_sliders, col_resultado = st.columns([1, 1])

with col_sliders:
    st.markdown("**Variables del escenario**")
    ajuste_tendencia = st.slider("Tendencia reciente (ventas de los últimos meses)", -30, 30, 0, format="%d%%")
    ajuste_estacionalidad = st.slider("Estacionalidad esperada (ej. campaña escolar)", -30, 30, 0, format="%d%%")
    if st.button("Restablecer"):
        st.rerun()

fila_features = resultado.df_features[
    (resultado.df_features["titulo"] == titulo)
    & resultado.df_features["ventas"].isna()
    & resultado.df_features[list(FEATURE_COLUMNS)].notna().all(axis=1)
]

with col_resultado:
    st.markdown("**Resultado del escenario**")
    if fila_features.empty:
        st.info("No hay suficiente historial continuo para simular este título.")
    else:
        X = fila_features[list(FEATURE_COLUMNS)].copy()
        columnas_tendencia = ["lag_1", "lag_2", "lag_3", "rolling_mean_3", "rolling_mean_6"]
        X[columnas_tendencia] = X[columnas_tendencia] * (1 + ajuste_tendencia / 100)

        demanda_base = resultado.modelo_activo.predict(X)[0]
        demanda_proyectada = demanda_base * (1 + ajuste_estacionalidad / 100)
        tiraje = float(recommend_print_run(np.array([demanda_proyectada]))[0])

        stock_actual = resumen.loc[titulo, "stock_actual_estimado"]
        prob_quiebre = max(0.0, min(100.0, (demanda_proyectada - stock_actual) / demanda_proyectada * 100)) \
            if demanda_proyectada > stock_actual else 0.0
        prob_sobrestock = max(0.0, min(100.0, (stock_actual - demanda_proyectada) / stock_actual * 100)) \
            if stock_actual > demanda_proyectada else 0.0

        st.metric("Demanda proyectada", f"{demanda_proyectada:,.0f} unidades")
        st.metric("Tiraje recomendado", f"{tiraje:,.0f} unidades")
        st.metric("Probabilidad de quiebre (estimada)", f"{prob_quiebre:.0f}%")
        st.metric("Probabilidad de sobrestock (estimada)", f"{prob_sobrestock:.0f}%")
        st.progress(int(resumen.loc[titulo, "confianza_modelo"]), text="Confianza del modelo")
