from fastapi import APIRouter, Depends

from api import service
from api.deps import get_pipeline_result
from api.schemas import ConfiguracionResponse

router = APIRouter(tags=["configuracion"])


@router.get("/configuracion", response_model=ConfiguracionResponse)
def configuracion(resultado=Depends(get_pipeline_result)):
    return service.get_configuracion(resultado)
