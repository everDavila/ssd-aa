import io

import streamlit as st

from ssd_aa import config
from ssd_aa.ui.state import get_pipeline_result

st.markdown("### 📄 Reportes y ⚙️ Configuración")

resultado = get_pipeline_result()

tab_reportes, tab_config = st.tabs(["Reportes", "Configuración"])

with tab_reportes:
    st.markdown("**Exportar recomendaciones de tiraje (todos los títulos)**")
    tabla = resultado.resumen_titulos[[
        "titulo", "autor", "genero", "demanda_prevista", "tiraje_recomendado",
        "stock_actual_estimado", "riesgo", "confianza_modelo",
    ]]
    csv = tabla.to_csv(index=False).encode("utf-8")
    st.download_button("Descargar CSV", data=csv, file_name="recomendaciones_tiraje.csv", mime="text/csv")

    buffer = io.BytesIO()
    tabla.to_excel(buffer, index=False, engine="openpyxl")
    st.download_button(
        "Descargar Excel", data=buffer.getvalue(), file_name="recomendaciones_tiraje.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    st.dataframe(tabla, hide_index=True, width="stretch")

with tab_config:
    st.markdown("**Parámetros activos del pipeline** (solo lectura en este MVP)")
    st.write(
        f"- Colchón de seguridad sobre el pronóstico: **{config.PRINT_RUN_SAFETY_BUFFER:.0%}**\n"
        f"- Umbral de riesgo bajo: desviación ≤ **{config.RISK_LOW_MAX_DEVIATION:.0%}**\n"
        f"- Umbral de riesgo medio: desviación ≤ **{config.RISK_MEDIUM_MAX_DEVIATION:.0%}**\n"
        f"- Meses de prueba por título (split temporal): **{config.TEST_MONTHS_PER_TITLE}**\n"
        f"- Ventana del método empírico (baseline): **{config.BASELINE_WINDOW_MONTHS} meses**\n"
        f"- Versión del modelo activo: **{config.MODEL_VERSION}**"
    )
    st.caption(
        "Para cambiar estos parámetros en esta iteración del MVP, edita "
        "`ssd_aa/config.py` y reinicia la aplicación. Un panel editable en "
        "vivo es una mejora natural para la siguiente iteración."
    )
