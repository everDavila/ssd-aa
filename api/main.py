from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.deps import get_pipeline_result
from api.routers import alertas, catalogo, configuracion, dashboard, modelos, reportes, simulador
from api.schemas import HealthResponse

app = FastAPI(title="SSD Editorial API")

# Defensa en profundidad: el navegador nunca debería llamar a este puerto
# directamente (Next.js actúa como BFF), pero se restringe CORS igual para
# poder probar /docs desde el navegador en desarrollo.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.include_router(dashboard.router, prefix="/api")
app.include_router(catalogo.router, prefix="/api")
app.include_router(reportes.router, prefix="/api")
app.include_router(alertas.router, prefix="/api")
app.include_router(modelos.router, prefix="/api")
app.include_router(simulador.router, prefix="/api")
app.include_router(configuracion.router, prefix="/api")


@app.get("/api/health", response_model=HealthResponse)
def health(resultado=Depends(get_pipeline_result)):
    return {
        "status": "ok",
        "modelo_ganador": resultado.modelo_ganador,
        "mape_test": resultado.metadata_modelo["mape_test"],
    }
