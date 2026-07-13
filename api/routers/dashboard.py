from fastapi import APIRouter, Depends

from api import service
from api.deps import get_pipeline_result
from api.schemas import DashboardResponse

router = APIRouter(tags=["dashboard"])


@router.get("/dashboard", response_model=DashboardResponse)
def dashboard(resultado=Depends(get_pipeline_result)):
    return service.get_dashboard(resultado)
