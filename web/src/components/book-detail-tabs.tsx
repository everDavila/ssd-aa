"use client";

import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { RiskBadge } from "@/components/risk-badge";
import { DemandChart } from "@/components/charts/demand-chart";
import { ShapChart } from "@/components/charts/shap-chart";
import { formatMonth } from "@/lib/format";
import type { CatalogoDetalleResponse } from "@/lib/types";

export function BookDetailTabs({ data }: { data: CatalogoDetalleResponse }) {
  if (!data.tiene_historial || !data.resumen) {
    return (
      <div className="flex flex-col gap-2">
        <h2 className="text-lg font-semibold">{data.titulo}</h2>
        <p className="text-sm text-muted-foreground">{data.autor} · {data.genero}</p>
        <div className="mt-4 rounded-xl border border-dashed border-border p-8 text-center text-muted-foreground">
          Este título todavía no tiene historial de ventas registrado, por lo que no
          participa del pronóstico ML. Acción sugerida: recolectar ventas
          históricas 2022–2025.
        </div>
      </div>
    );
  }

  const { resumen } = data;

  return (
    <div className="flex flex-col gap-4">
      <div>
        <h2 className="text-lg font-semibold">{data.titulo}</h2>
        <p className="text-sm text-muted-foreground">{data.autor} · {data.genero}</p>
      </div>

      <div className="grid grid-cols-2 gap-4 lg:grid-cols-4">
        <div className="rounded-xl border border-border bg-card p-4">
          <div className="text-xs text-muted-foreground">Stock actual (estimado)</div>
          <div className="text-xl font-semibold">{resumen.stock_actual_estimado.toLocaleString()} u.</div>
        </div>
        <div className="rounded-xl border border-border bg-card p-4">
          <div className="text-xs text-muted-foreground">Demanda prevista</div>
          <div className="text-xl font-semibold">
            {resumen.demanda_prevista.toLocaleString(undefined, { maximumFractionDigits: 0 })} u.
          </div>
        </div>
        <div className="rounded-xl border border-border bg-card p-4">
          <div className="text-xs text-muted-foreground">Tiraje recomendado</div>
          <div className="text-xl font-semibold">{resumen.tiraje_recomendado.toLocaleString()} u.</div>
        </div>
        <div className="flex flex-col justify-center rounded-xl border border-border bg-card p-4">
          <div className="mb-1 text-xs text-muted-foreground">Riesgo</div>
          <RiskBadge nivel={resumen.riesgo} />
        </div>
      </div>

      <Tabs defaultValue="resumen">
        <TabsList>
          <TabsTrigger value="resumen">Resumen</TabsTrigger>
          <TabsTrigger value="prediccion">Predicción</TabsTrigger>
          <TabsTrigger value="factores">Factores</TabsTrigger>
          <TabsTrigger value="historial">Historial</TabsTrigger>
          <TabsTrigger value="recomendacion">Recomendación</TabsTrigger>
        </TabsList>

        <TabsContent value="resumen">
          <div className="grid max-w-md grid-cols-2 gap-y-2 rounded-xl border border-border bg-card p-4 text-sm">
            <span className="text-muted-foreground">Formato</span>
            <span>{data.formato ?? "—"}</span>
            <span className="text-muted-foreground">N.° páginas</span>
            <span>{data.n_paginas ?? "—"}</span>
            <span className="text-muted-foreground">PVP mayor (S/.)</span>
            <span>{data.pvp ?? "—"}</span>
          </div>
        </TabsContent>

        <TabsContent value="prediccion">
          <div className="rounded-xl border border-border bg-card p-4">
            <DemandChart data={data.historial ?? []} />
            <p className="mt-3 text-sm">
              Demanda esperada (próximo mes): <b>{resumen.demanda_prevista.toLocaleString(undefined, { maximumFractionDigits: 0 })} unidades</b><br />
              Tiraje recomendado: <b>{resumen.tiraje_recomendado.toLocaleString()} unidades</b> (colchón de seguridad incluido)<br />
              Confianza del modelo: <b>{resumen.confianza_modelo.toFixed(0)}%</b>{" "}
              <span className="text-xs text-muted-foreground">
                (heurística: 100 − MAPE de prueba, no una probabilidad calibrada)
              </span>
            </p>
          </div>
        </TabsContent>

        <TabsContent value="factores">
          <div className="rounded-xl border border-border bg-card p-4">
            {data.factores && data.factores.length > 0 ? (
              <>
                <ShapChart data={data.factores} />
                <p className="mt-2 text-xs text-muted-foreground">
                  Factores reales que usa el modelo (ventas recientes, tendencia,
                  estacionalidad, perfil del título) — no las variables ilustrativas
                  del mockup original (campaña escolar, publicidad, competencia),
                  que no existen en los datos.
                </p>
              </>
            ) : (
              <p className="text-sm text-muted-foreground">
                No hay suficiente historial continuo para explicar esta predicción.
              </p>
            )}
          </div>
        </TabsContent>

        <TabsContent value="historial">
          <div className="overflow-hidden rounded-xl border border-border bg-card">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Mes</TableHead>
                  <TableHead>Ventas reales</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {(data.historial ?? []).map((punto) => (
                  <TableRow key={punto.fecha}>
                    <TableCell>{formatMonth(punto.fecha)}</TableCell>
                    <TableCell>{punto.ventas.toLocaleString()}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        </TabsContent>

        <TabsContent value="recomendacion">
          <div className="flex flex-col items-start gap-3 rounded-xl border border-border bg-card p-4">
            <p>{data.recomendacion_texto}</p>
            <a
              href={`/api/reportes/orden-impresion/${data.id_titulo}`}
              className="inline-flex h-9 items-center rounded-lg bg-primary px-4 text-sm font-medium text-primary-foreground hover:opacity-90"
            >
              Generar orden de impresión (CSV)
            </a>
          </div>
        </TabsContent>
      </Tabs>
    </div>
  );
}
