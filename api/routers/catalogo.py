from fastapi import APIRouter, Depends, HTTPException, Query

from api import service
from api.deps import get_pipeline_result
from api.schemas import CatalogoDetalleResponse, CatalogoListResponse

router = APIRouter(tags=["catalogo"])


@router.get("/catalogo", response_model=CatalogoListResponse)
def listar(
    q: str | None = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    riesgo: str | None = None,
    resultado=Depends(get_pipeline_result),
):
    return service.list_catalogo(resultado, q=q, page=page, page_size=page_size, riesgo=riesgo)


@router.get("/catalogo/{id_titulo}", response_model=CatalogoDetalleResponse)
def detalle(id_titulo: str, resultado=Depends(get_pipeline_result)):
    data = service.get_catalogo_detalle(resultado, id_titulo)
    if data is None:
        raise HTTPException(status_code=404, detail="Título no encontrado en el catálogo")
    return data
