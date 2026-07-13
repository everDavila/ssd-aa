from fastapi import APIRouter, Depends, HTTPException

from api import service
from api.deps import get_pipeline_result
from api.schemas import SimuladorRequest, SimuladorResponse

router = APIRouter(tags=["simulador"])


@router.post("/simulador", response_model=SimuladorResponse)
def simular(payload: SimuladorRequest, resultado=Depends(get_pipeline_result)):
    resultado_simulacion = service.simulate_scenario(
        resultado,
        id_titulo=payload.id_titulo,
        ajuste_tendencia=payload.ajuste_tendencia,
        ajuste_estacionalidad=payload.ajuste_estacionalidad,
    )
    if resultado_simulacion is None:
        raise HTTPException(
            status_code=422,
            detail="Título no encontrado o sin suficiente historial continuo para simular.",
        )
    return resultado_simulacion
