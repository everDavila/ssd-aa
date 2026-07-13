import Link from "next/link";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { getConfiguracion } from "@/lib/api";

export default async function ReportesPage() {
  const config = await getConfiguracion();

  return (
    <Tabs defaultValue="reportes">
      <TabsList>
        <TabsTrigger value="reportes">Reportes</TabsTrigger>
        <TabsTrigger value="configuracion">Configuración</TabsTrigger>
      </TabsList>

      <TabsContent value="reportes">
        <div className="flex flex-col gap-4 rounded-xl border border-border bg-card p-4">
          <h3 className="font-medium">Exportar recomendaciones de tiraje (todos los títulos con historial)</h3>
          <div className="flex gap-2">
            <Link
              href="/api/reportes/recomendaciones/csv"
              className="inline-flex h-9 items-center rounded-lg bg-primary px-4 text-sm font-medium text-primary-foreground hover:opacity-90"
            >
              Descargar CSV
            </Link>
            <Link
              href="/api/reportes/recomendaciones/xlsx"
              className="inline-flex h-9 items-center rounded-lg border border-border bg-card px-4 text-sm font-medium hover:bg-accent"
            >
              Descargar Excel
            </Link>
          </div>
        </div>
      </TabsContent>

      <TabsContent value="configuracion">
        <div className="flex flex-col gap-2 rounded-xl border border-border bg-card p-4 text-sm">
          <h3 className="mb-2 font-medium">Parámetros activos del pipeline (solo lectura en este MVP)</h3>
          <ul className="list-inside list-disc space-y-1">
            <li>Colchón de seguridad sobre el pronóstico: <b>{(config.print_run_safety_buffer * 100).toFixed(0)}%</b></li>
            <li>Umbral de riesgo bajo: desviación ≤ <b>{(config.risk_low_max_deviation * 100).toFixed(0)}%</b></li>
            <li>Umbral de riesgo medio: desviación ≤ <b>{(config.risk_medium_max_deviation * 100).toFixed(0)}%</b></li>
            <li>Meses de prueba por título (split temporal): <b>{config.test_months_per_title}</b></li>
            <li>Ventana del método empírico (baseline): <b>{config.baseline_window_months} meses</b></li>
            <li>Versión del modelo activo: <b>{config.model_version}</b> ({config.modelo_activo})</li>
          </ul>
          <p className="mt-2 text-xs text-muted-foreground">
            Para cambiar estos parámetros en esta iteración del MVP, edita
            <code> ssd_aa/config.py</code> y reinicia la API. Un panel editable en
            vivo es una mejora natural para la siguiente iteración.
          </p>
        </div>
      </TabsContent>
    </Tabs>
  );
}
