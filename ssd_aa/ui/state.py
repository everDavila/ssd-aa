"""Estado compartido entre páginas: el pipeline se entrena una sola vez por
sesión de servidor y se reutiliza en Dashboard/Catálogo/Detalle/Alertas/etc."""

import streamlit as st

from ssd_aa.pipeline import PipelineResult, run_pipeline


@st.cache_resource(show_spinner="Entrenando modelos y generando pronósticos...")
def get_pipeline_result() -> PipelineResult:
    return run_pipeline()
