import "server-only";
import type {
  AlertasResponse,
  CatalogoDetalleResponse,
  CatalogoListResponse,
  ConfiguracionResponse,
  DashboardResponse,
  ModelosResponse,
  SimuladorRequest,
  SimuladorResponse,
} from "@/lib/types";

const BASE_URL = process.env.SSD_API_BASE_URL ?? "http://127.0.0.1:8000";

async function apiFetch<T>(path: string): Promise<T> {
  const res = await fetch(`${BASE_URL}${path}`, { cache: "no-store" });
  if (!res.ok) {
    throw new Error(`SSD API ${path} -> HTTP ${res.status}`);
  }
  return res.json() as Promise<T>;
}

export function getDashboard() {
  return apiFetch<DashboardResponse>("/api/dashboard");
}

export function getCatalogo(params: {
  q?: string;
  page?: number;
  pageSize?: number;
  riesgo?: string;
}) {
  const search = new URLSearchParams();
  if (params.q) search.set("q", params.q);
  if (params.page) search.set("page", String(params.page));
  if (params.pageSize) search.set("page_size", String(params.pageSize));
  if (params.riesgo && params.riesgo !== "Todas") search.set("riesgo", params.riesgo);
  return apiFetch<CatalogoListResponse>(`/api/catalogo?${search.toString()}`);
}

export async function getCatalogoDetalle(idTitulo: string): Promise<CatalogoDetalleResponse | null> {
  const res = await fetch(`${BASE_URL}/api/catalogo/${encodeURIComponent(idTitulo)}`, { cache: "no-store" });
  if (res.status === 404) return null;
  if (!res.ok) throw new Error(`SSD API /api/catalogo/${idTitulo} -> HTTP ${res.status}`);
  return res.json();
}

export function getAlertas(riesgo?: string) {
  const search = new URLSearchParams();
  if (riesgo && riesgo !== "Todas") search.set("riesgo", riesgo);
  return apiFetch<AlertasResponse>(`/api/alertas?${search.toString()}`);
}

export function getModelos() {
  return apiFetch<ModelosResponse>("/api/modelos");
}

export function getConfiguracion() {
  return apiFetch<ConfiguracionResponse>("/api/configuracion");
}

export async function simulateScenario(payload: SimuladorRequest): Promise<SimuladorResponse | null> {
  const res = await fetch(`${BASE_URL}/api/simulador`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
    cache: "no-store",
  });
  if (res.status === 422) return null;
  if (!res.ok) throw new Error(`SSD API /api/simulador -> HTTP ${res.status}`);
  return res.json();
}
