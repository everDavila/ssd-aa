"""Cachea el resultado del pipeline a nivel de proceso — equivalente a
`st.cache_resource` fuera de Streamlit. Requiere correr uvicorn con
--workers 1 (el cache no se comparte entre procesos)."""

from functools import lru_cache

from ssd_aa.pipeline import PipelineResult, run_pipeline


@lru_cache(maxsize=1)
def get_pipeline_result() -> PipelineResult:
    return run_pipeline()
