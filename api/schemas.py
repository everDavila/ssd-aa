"""Contratos de respuesta de la API. Reflejan lo que ssd_aa.pipeline ya
calcula — no se recalcula ni se inventa ningún número aquí."""

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    modelo_ganador: str
    mape_test: float


class SeriePunto(BaseModel):
    fecha: str
    ventas: float


class KpisDashboard(BaseModel):
    mape_actual: float
    mape_delta: float
    sobrestock_pct: float
    sobrestock_delta: float
    quiebre_pct: float
    quiebre_delta: float
    tiempo_proceso_seg: float


class TopRiesgoItem(BaseModel):
    id_titulo: str
    titulo: str
    demanda_prevista: float
    riesgo: str


class ChartDemanda(BaseModel):
    titulo: str
    serie: list[SeriePunto]


class TotalesDashboard(BaseModel):
    total_catalogo: int
    titulos_activos: int
    pedidos_sugeridos: int
    tirada_total: int


class DashboardResponse(BaseModel):
    kpis: KpisDashboard
    top_riesgo: list[TopRiesgoItem]
    chart_demanda: ChartDemanda
    totales: TotalesDashboard


class CatalogoItem(BaseModel):
    id_titulo: str
    titulo: str
    autor: str
    genero: str
    demanda_prevista: float | None
    riesgo: str | None
    tiene_historial: bool


class CatalogoListResponse(BaseModel):
    items: list[CatalogoItem]
    page: int
    page_size: int
    total: int
    total_pages: int


class ResumenDetalle(BaseModel):
    stock_actual_estimado: float
    demanda_prevista: float
    tiraje_recomendado: float
    riesgo: str
    confianza_modelo: float


class FactorImpacto(BaseModel):
    factor: str
    impacto: float


class CatalogoDetalleResponse(BaseModel):
    id_titulo: str
    titulo: str
    autor: str
    genero: str
    formato: str | None
    n_paginas: float | None
    pvp: float | None
    tiene_historial: bool
    resumen: ResumenDetalle | None
    historial: list[SeriePunto] | None
    factores: list[FactorImpacto] | None
    recomendacion_texto: str | None


class AlertaItem(BaseModel):
    id_titulo: str
    titulo: str
    riesgo: str
    tipo_alerta: str  # "quiebre" | "sobrestock" | "demanda_inusual" | "normal"
    demanda_prevista: float
    stock_actual_estimado: float
    tiraje_recomendado: float
    mensaje: str


class AlertasResponse(BaseModel):
    conteos: dict[str, int]
    items: list[AlertaItem]


class ModeloItem(BaseModel):
    modelo: str
    mape: float | None
    mae: float | None
    rmse: float | None
    tiempo_entrenamiento_seg: float | None
    estado: str


class ModelosResponse(BaseModel):
    modelo_activo: str
    filas: list[ModeloItem]


class SimuladorRequest(BaseModel):
    id_titulo: str
    ajuste_tendencia: int = 0
    ajuste_estacionalidad: int = 0


class SimuladorResponse(BaseModel):
    demanda_proyectada: float
    tiraje_recomendado: float
    prob_quiebre: float
    prob_sobrestock: float
    confianza_modelo: float


class ConfiguracionResponse(BaseModel):
    print_run_safety_buffer: float
    risk_low_max_deviation: float
    risk_medium_max_deviation: float
    test_months_per_title: int
    baseline_window_months: int
    model_version: str
    modelo_activo: str


class RecomendacionItem(BaseModel):
    id_titulo: str
    titulo: str
    autor: str
    genero: str
    demanda_prevista: float
    tiraje_recomendado: float
    stock_actual_estimado: float
    riesgo: str
    confianza_modelo: float


class RecomendacionesResponse(BaseModel):
    items: list[RecomendacionItem]
