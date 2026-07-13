export type RiskLevel = "Bajo" | "Medio" | "Alto";

export type SeriePunto = { fecha: string; ventas: number };

export type KpisDashboard = {
  mape_actual: number;
  mape_delta: number;
  sobrestock_pct: number;
  sobrestock_delta: number;
  quiebre_pct: number;
  quiebre_delta: number;
  tiempo_proceso_seg: number;
};

export type TopRiesgoItem = {
  id_titulo: string;
  titulo: string;
  demanda_prevista: number;
  riesgo: RiskLevel;
};

export type DashboardResponse = {
  kpis: KpisDashboard;
  top_riesgo: TopRiesgoItem[];
  chart_demanda: { titulo: string; serie: SeriePunto[] };
  totales: {
    total_catalogo: number;
    titulos_activos: number;
    pedidos_sugeridos: number;
    tirada_total: number;
  };
};

export type CatalogoItem = {
  id_titulo: string;
  titulo: string;
  autor: string;
  genero: string;
  demanda_prevista: number | null;
  riesgo: RiskLevel | null;
  tiene_historial: boolean;
};

export type CatalogoListResponse = {
  items: CatalogoItem[];
  page: number;
  page_size: number;
  total: number;
  total_pages: number;
};

export type ResumenDetalle = {
  stock_actual_estimado: number;
  demanda_prevista: number;
  tiraje_recomendado: number;
  riesgo: RiskLevel;
  confianza_modelo: number;
};

export type FactorImpacto = { factor: string; impacto: number };

export type CatalogoDetalleResponse = {
  id_titulo: string;
  titulo: string;
  autor: string;
  genero: string;
  formato: string | null;
  n_paginas: number | null;
  pvp: number | null;
  tiene_historial: boolean;
  resumen: ResumenDetalle | null;
  historial: SeriePunto[] | null;
  factores: FactorImpacto[] | null;
  recomendacion_texto: string | null;
};

export type TipoAlerta = "quiebre" | "sobrestock" | "demanda_inusual" | "normal";

export type AlertaItem = {
  id_titulo: string;
  titulo: string;
  riesgo: RiskLevel;
  tipo_alerta: TipoAlerta;
  demanda_prevista: number;
  stock_actual_estimado: number;
  tiraje_recomendado: number;
  mensaje: string;
};

export type AlertasResponse = {
  conteos: Record<"Todas" | RiskLevel, number>;
  items: AlertaItem[];
};

export type ModeloItem = {
  modelo: string;
  mape: number | null;
  mae: number | null;
  rmse: number | null;
  tiempo_entrenamiento_seg: number | null;
  estado: "Activo" | "Disponible" | "Próximamente";
};

export type ModelosResponse = {
  modelo_activo: string;
  filas: ModeloItem[];
};

export type SimuladorRequest = {
  id_titulo: string;
  ajuste_tendencia: number;
  ajuste_estacionalidad: number;
};

export type SimuladorResponse = {
  demanda_proyectada: number;
  tiraje_recomendado: number;
  prob_quiebre: number;
  prob_sobrestock: number;
  confianza_modelo: number;
};

export type ConfiguracionResponse = {
  print_run_safety_buffer: number;
  risk_low_max_deviation: number;
  risk_medium_max_deviation: number;
  test_months_per_title: number;
  baseline_window_months: number;
  model_version: string;
  modelo_activo: string;
};
