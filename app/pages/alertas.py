import streamlit as st

from ssd_aa.ui.components import risk_label_with_emoji
from ssd_aa.ui.state import get_pipeline_result

st.markdown("### 🔔 Alertas")

resultado = get_pipeline_result()
resumen = resultado.resumen_titulos

conteo = resumen["riesgo"].value_counts()
etiquetas = ["Todas", "Alto", "Medio", "Bajo"]
opciones = {
    "Todas": f"Todas ({len(resumen)})",
    "Alto": f"Riesgo alto ({conteo.get('Alto', 0)})",
    "Medio": f"Riesgo medio ({conteo.get('Medio', 0)})",
    "Bajo": f"Riesgo bajo ({conteo.get('Bajo', 0)})",
}
filtro = st.radio("Filtrar por riesgo", etiquetas, format_func=lambda k: opciones[k], horizontal=True)

vista = resumen if filtro == "Todas" else resumen[resumen["riesgo"] == filtro]
vista = vista.sort_values("riesgo", key=lambda s: s.map({"Alto": 0, "Medio": 1, "Bajo": 2}))

for _, fila in vista.iterrows():
    delta_demanda = fila["demanda_prevista"] - fila["stock_actual_estimado"]
    with st.container(border=True):
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown(f"**{risk_label_with_emoji(fila['riesgo'])} — {fila['titulo']}**")
            if fila["riesgo"] == "Alto" and delta_demanda > 0:
                st.write(
                    f"Riesgo de desabastecimiento: la demanda esperada "
                    f"({fila['demanda_prevista']:,.0f}) supera el stock estimado "
                    f"({fila['stock_actual_estimado']:,.0f})."
                )
            elif fila["riesgo"] == "Alto":
                st.write(
                    f"Posible sobrestock: el stock estimado "
                    f"({fila['stock_actual_estimado']:,.0f}) excede ampliamente "
                    f"la demanda prevista ({fila['demanda_prevista']:,.0f})."
                )
            elif fila["riesgo"] == "Medio":
                st.write(
                    f"Desviación moderada entre demanda prevista "
                    f"({fila['demanda_prevista']:,.0f}) y stock estimado "
                    f"({fila['stock_actual_estimado']:,.0f})."
                )
            else:
                st.write("Demanda y stock estimado dentro de los parámetros normales.")
        with c2:
            st.metric("Tiraje recomendado", f"{fila['tiraje_recomendado']:,.0f}")
