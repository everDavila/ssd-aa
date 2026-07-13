import Link from "next/link";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { RiskBadge } from "@/components/risk-badge";
import { getCatalogo } from "@/lib/api";
import { cn } from "@/lib/utils";

const FILTROS_RIESGO = ["Todas", "Alto", "Medio", "Bajo"] as const;
const PAGE_SIZE = 20;

function buildQuery(params: Record<string, string | number | undefined>) {
  const search = new URLSearchParams();
  for (const [key, value] of Object.entries(params)) {
    if (value !== undefined && value !== "" && value !== "Todas") search.set(key, String(value));
  }
  const qs = search.toString();
  return qs ? `?${qs}` : "";
}

export default async function CatalogoPage({
  searchParams,
}: {
  searchParams: Promise<{ q?: string; page?: string; riesgo?: string }>;
}) {
  const { q, page: pageParam, riesgo } = await searchParams;
  const page = Number(pageParam ?? 1) || 1;

  const data = await getCatalogo({ q, page, pageSize: PAGE_SIZE, riesgo });

  return (
    <div className="flex flex-col gap-4">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <form className="flex gap-2" action="/catalogo">
          <Input name="q" defaultValue={q} placeholder="Buscar por título o autor…" className="w-72" />
          <Button type="submit" variant="secondary">Buscar</Button>
        </form>

        <div className="flex gap-2">
          {FILTROS_RIESGO.map((nivel) => (
            <Link
              key={nivel}
              href={`/catalogo${buildQuery({ q, riesgo: nivel })}`}
              className={cn(
                "rounded-full border px-3 py-1 text-sm font-medium",
                (riesgo ?? "Todas") === nivel
                  ? "border-primary bg-primary text-primary-foreground"
                  : "border-border bg-card text-muted-foreground hover:bg-accent"
              )}
            >
              {nivel}
            </Link>
          ))}
        </div>
      </div>

      <div className="overflow-hidden rounded-xl border border-border bg-card">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Título</TableHead>
              <TableHead>Autor</TableHead>
              <TableHead>Categoría</TableHead>
              <TableHead>Demanda prevista</TableHead>
              <TableHead>Riesgo</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {data.items.map((item) => (
              <TableRow key={item.id_titulo}>
                <TableCell className="font-medium">
                  {item.tiene_historial ? (
                    <Link href={`/catalogo/${item.id_titulo}`} className="hover:underline">
                      {item.titulo}
                    </Link>
                  ) : (
                    item.titulo
                  )}
                </TableCell>
                <TableCell>{item.autor}</TableCell>
                <TableCell>{item.genero}</TableCell>
                <TableCell>
                  {item.demanda_prevista != null
                    ? item.demanda_prevista.toLocaleString(undefined, { maximumFractionDigits: 0 })
                    : "—"}
                </TableCell>
                <TableCell>
                  {item.riesgo ? <RiskBadge nivel={item.riesgo} /> : (
                    <span className="text-xs text-muted-foreground">Sin historial</span>
                  )}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>

      <div className="flex items-center justify-between text-sm text-muted-foreground">
        <span>
          {data.total} títulos · página {data.page} de {data.total_pages}
        </span>
        <div className="flex gap-2">
          <Link
            href={`/catalogo${buildQuery({ q, riesgo, page: Math.max(1, page - 1) })}`}
            aria-disabled={page <= 1}
            className={cn(
              "rounded-lg border border-border px-3 py-1",
              page <= 1 ? "pointer-events-none opacity-40" : "hover:bg-accent"
            )}
          >
            Anterior
          </Link>
          <Link
            href={`/catalogo${buildQuery({ q, riesgo, page: Math.min(data.total_pages, page + 1) })}`}
            aria-disabled={page >= data.total_pages}
            className={cn(
              "rounded-lg border border-border px-3 py-1",
              page >= data.total_pages ? "pointer-events-none opacity-40" : "hover:bg-accent"
            )}
          >
            Siguiente
          </Link>
        </div>
      </div>
    </div>
  );
}
