import pandas as pd
import streamlit as st

from ssd_aa.ui.components import model_comparison_chart
from ssd_aa.ui.state import get_pipeline_result

st.markdown("### 🤖 Comparación de Modelos")

resultado = get_pipeline_result()
comparacion = resultado.comparacion_modelos.copy()
comparacion["Estado"] = comparacion["modelo"].map(
    lambda m: "✅ Activo" if m == resultado.modelo_ganador else "Disponible"
)

lstm_fila = pd.DataFrame([{
    "modelo": "LSTM", "mape": None, "mae": None, "rmse": None,
    "tiempo_entrenamiento_seg": None, "Estado": "🚧 Próximamente",
}])
tabla = pd.concat([comparacion, lstm_fila], ignore_index=True)

st.dataframe(
    tabla.rename(columns={
        "modelo": "Modelo", "mape": "MAPE (%)", "mae": "MAE", "rmse": "RMSE",
        "tiempo_entrenamiento_seg": "Tiempo de entrenamiento (s)",
    }),
    hide_index=True, width="stretch",
)
st.caption(
    "LSTM requiere TensorFlow y ventanas de secuencia por título; se deja "
    "fuera de este MVP porque, con el volumen real de datos disponible, no "
    "hay evidencia de que supere a los 3 modelos ya entrenados aquí."
)

st.plotly_chart(model_comparison_chart(comparacion), width="stretch")

st.markdown("**Modelo activo**")
st.info(
    f"**{resultado.modelo_ganador}** — modelo con menor MAPE de prueba "
    f"({resultado.metadata_modelo['mape_test']:.2f}%) entre los evaluados."
)
