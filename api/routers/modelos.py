from fastapi import APIRouter, Depends

from api import service
from api.deps import get_pipeline_result
from api.schemas import ModelosResponse

router = APIRouter(tags=["modelos"])


@router.get("/modelos", response_model=ModelosResponse)
def modelos(resultado=Depends(get_pipeline_result)):
    return service.get_modelos(resultado)
