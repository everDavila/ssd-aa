from fastapi import APIRouter, Depends

from api import service
from api.deps import get_pipeline_result
from api.schemas import AlertasResponse

router = APIRouter(tags=["alertas"])


@router.get("/alertas", response_model=AlertasResponse)
def alertas(riesgo: str | None = None, resultado=Depends(get_pipeline_result)):
    return service.get_alertas(resultado, riesgo=riesgo)
