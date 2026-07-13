from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response

from api import service
from api.deps import get_pipeline_result

router = APIRouter(tags=["reportes"])


@router.get("/reportes/orden-impresion/{id_titulo}.csv")
def orden_impresion(id_titulo: str, resultado=Depends(get_pipeline_result)):
    csv = service.orden_impresion_csv(resultado, id_titulo)
    if csv is None:
        raise HTTPException(status_code=404, detail="Título no encontrado")
    return Response(
        content=csv,
        media_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="orden_impresion_{id_titulo}.csv"'},
    )


@router.get("/reportes/recomendaciones.csv")
def recomendaciones_csv(resultado=Depends(get_pipeline_result)):
    return Response(
        content=service.recomendaciones_csv(resultado),
        media_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="recomendaciones_tiraje.csv"'},
    )


@router.get("/reportes/recomendaciones.xlsx")
def recomendaciones_xlsx(resultado=Depends(get_pipeline_result)):
    return Response(
        content=service.recomendaciones_xlsx(resultado),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": 'attachment; filename="recomendaciones_tiraje.xlsx"'},
    )
