import Link from "next/link";
import { RiskBadge } from "@/components/risk-badge";
import { getAlertas } from "@/lib/api";
import { cn } from "@/lib/utils";
import type { RiskLevel } from "@/lib/types";

const FILTROS = ["Todas", "Alto", "Medio", "Bajo"] as const;

export default async function AlertasPage({
  searchParams,
}: {
  searchParams: Promise<{ riesgo?: string }>;
}) {
  const { riesgo } = await searchParams;
  const filtroActivo = (riesgo ?? "Todas") as (typeof FILTROS)[number];
  const data = await getAlertas(riesgo);

  return (
    <div className="flex flex-col gap-4">
      <div className="flex flex-wrap gap-2">
        {FILTROS.map((nivel) => (
          <Link
            key={nivel}
            href={nivel === "Todas" ? "/alertas" : `/alertas?riesgo=${nivel}`}
            className={cn(
              "rounded-full border px-3 py-1.5 text-sm font-medium",
              filtroActivo === nivel
                ? "border-primary bg-primary text-primary-foreground"
                : "border-border bg-card text-muted-foreground hover:bg-accent"
            )}
          >
            {nivel === "Todas" ? "Todas" : `Riesgo ${nivel.toLowerCase()}`} ({data.conteos[nivel]})
          </Link>
        ))}
      </div>

      <div className="flex flex-col gap-3">
        {data.items.map((item) => (
          <div key={item.id_titulo} className="flex items-center justify-between rounded-xl border border-border bg-card p-4">
            <div>
              <div className="flex items-center gap-2 font-medium">
                <RiskBadge nivel={item.riesgo as RiskLevel} />
                <Link href={`/catalogo/${item.id_titulo}`} className="hover:underline">
                  {item.titulo}
                </Link>
              </div>
              <p className="mt-1 text-sm text-muted-foreground">{item.mensaje}</p>
            </div>
            <div className="text-right">
              <div className="text-xs text-muted-foreground">Tiraje recomendado</div>
              <div className="text-lg font-semibold">{item.tiraje_recomendado.toLocaleString()}</div>
            </div>
          </div>
        ))}
        {data.items.length === 0 && (
          <p className="text-sm text-muted-foreground">No hay alertas para este filtro.</p>
        )}
      </div>
    </div>
  );
}
