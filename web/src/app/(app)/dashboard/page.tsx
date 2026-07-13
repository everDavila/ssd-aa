import Link from "next/link";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { KpiCard } from "@/components/kpi-card";
import { RiskBadge } from "@/components/risk-badge";
import { DemandChart } from "@/components/charts/demand-chart";
import { getDashboard } from "@/lib/api";

export default async function DashboardPage() {
  const data = await getDashboard();
  const k = data.kpis;

  return (
    <div className="flex flex-col gap-6">
      <div className="grid grid-cols-2 gap-4 lg:grid-cols-4">
        <KpiCard label="MAPE actual" value={`${k.mape_actual.toFixed(2)}%`} delta={`${k.mape_delta.toFixed(2)} pp vs. método tradicional`} deltaDirection={k.mape_delta <= 0 ? "down" : "up"} deltaTone={k.mape_delta <= 0 ? "good" : "bad"} />
        <KpiCard label="Sobrestock" value={`${k.sobrestock_pct.toFixed(2)}%`} delta={`${k.sobrestock_delta.toFixed(2)} pp vs. método tradicional`} deltaDirection={k.sobrestock_delta <= 0 ? "down" : "up"} deltaTone={k.sobrestock_delta <= 0 ? "good" : "bad"} />
        <KpiCard label="Quiebre de stock" value={`${k.quiebre_pct.toFixed(2)}%`} delta={`${k.quiebre_delta >= 0 ? "+" : ""}${k.quiebre_delta.toFixed(2)} pp vs. método tradicional`} deltaDirection={k.quiebre_delta <= 0 ? "down" : "up"} deltaTone={k.quiebre_delta <= 0 ? "good" : "bad"} />
        <KpiCard label="Tiempo de proceso" value={`${k.tiempo_proceso_seg.toFixed(2)} s`} />
      </div>

      <div className="grid grid-cols-1 gap-4 lg:grid-cols-3">
        <Card className="lg:col-span-2">
          <CardHeader>
            <CardTitle>Demanda: histórico vs. predicción — {data.chart_demanda.titulo}</CardTitle>
          </CardHeader>
          <CardContent>
            <DemandChart data={data.chart_demanda.serie} />
            <p className="mt-2 text-xs text-muted-foreground">
              El pipeline pronostica 1 mes hacia adelante (no 6, como el mockup ilustrativo original)
              dado el horizonte real de datos disponible por título.
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Libros con mayor riesgo</CardTitle>
          </CardHeader>
          <CardContent className="flex flex-col gap-3">
            {data.top_riesgo.map((libro) => (
              <Link
                key={libro.id_titulo}
                href={`/catalogo/${libro.id_titulo}`}
                className="flex items-center justify-between rounded-lg px-2 py-1.5 hover:bg-accent"
              >
                <div>
                  <div className="text-sm font-medium">{libro.titulo}</div>
                  <div className="text-xs text-muted-foreground">
                    {libro.demanda_prevista.toLocaleString(undefined, { maximumFractionDigits: 0 })} unidades
                  </div>
                </div>
                <RiskBadge nivel={libro.riesgo} />
              </Link>
            ))}
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-2 gap-4 lg:grid-cols-4">
        <KpiCard label="Total de títulos (catálogo)" value={String(data.totales.total_catalogo)} />
        <KpiCard label="Títulos con pronóstico ML" value={String(data.totales.titulos_activos)} />
        <KpiCard label="Pedidos sugeridos" value={String(data.totales.pedidos_sugeridos)} />
        <KpiCard label="Tirada recomendada total" value={data.totales.tirada_total.toLocaleString()} />
      </div>
    </div>
  );
}
