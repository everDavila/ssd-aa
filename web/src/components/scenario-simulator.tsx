"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Slider } from "@/components/ui/slider";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import type { SimuladorResponse } from "@/lib/types";

type Opcion = { id_titulo: string; titulo: string };
type Escenario = { idTitulo: string; tendencia: number; estacionalidad: number };

async function simular(escenario: Escenario): Promise<SimuladorResponse> {
  const res = await fetch("/api/simulador", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      id_titulo: escenario.idTitulo,
      ajuste_tendencia: escenario.tendencia,
      ajuste_estacionalidad: escenario.estacionalidad,
    }),
  });
  if (!res.ok) {
    const body = await res.json().catch(() => null);
    throw new Error(body?.detail ?? `Error ${res.status}`);
  }
  return res.json();
}

export function ScenarioSimulator({
  opciones,
  idTituloInicial,
  resultadoInicial,
}: {
  opciones: Opcion[];
  idTituloInicial: string;
  resultadoInicial: SimuladorResponse | null;
}) {
  const router = useRouter();
  const [idTitulo, setIdTitulo] = useState(idTituloInicial);
  const [ajusteTendencia, setAjusteTendencia] = useState(0);
  const [ajusteEstacionalidad, setAjusteEstacionalidad] = useState(0);
  const [resultado, setResultado] = useState<SimuladorResponse | null>(resultadoInicial);
  const [error, setError] = useState<string | null>(null);
  const [cargando, setCargando] = useState(false);

  async function ejecutar(escenario: Escenario) {
    setCargando(true);
    setError(null);
    try {
      setResultado(await simular(escenario));
    } catch (err) {
      setError(err instanceof Error ? err.message : "Error al simular el escenario.");
      setResultado(null);
    } finally {
      setCargando(false);
    }
  }

  function handleCambioTitulo(nuevoId: string | null) {
    if (!nuevoId) return;
    setIdTitulo(nuevoId);
    setAjusteTendencia(0);
    setAjusteEstacionalidad(0);
    router.replace(`/simulador?id=${nuevoId}`);
    ejecutar({ idTitulo: nuevoId, tendencia: 0, estacionalidad: 0 });
  }

  return (
    <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
      <div className="flex flex-col gap-4 rounded-xl border border-border bg-card p-4">
        <div>
          <label className="mb-1 block text-sm font-medium">Título</label>
          <Select value={idTitulo} onValueChange={handleCambioTitulo}>
            <SelectTrigger className="w-full">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              {opciones.map((op) => (
                <SelectItem key={op.id_titulo} value={op.id_titulo}>
                  {op.titulo}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        <div>
          <label className="mb-2 block text-sm font-medium">
            Tendencia reciente (ventas de los últimos meses): {ajusteTendencia >= 0 ? "+" : ""}
            {ajusteTendencia}%
          </label>
          <Slider
            value={[ajusteTendencia]}
            min={-30}
            max={30}
            step={1}
            onValueChange={(v) => setAjusteTendencia(Array.isArray(v) ? v[0] : v)}
          />
        </div>

        <div>
          <label className="mb-2 block text-sm font-medium">
            Estacionalidad esperada (ej. campaña escolar): {ajusteEstacionalidad >= 0 ? "+" : ""}
            {ajusteEstacionalidad}%
          </label>
          <Slider
            value={[ajusteEstacionalidad]}
            min={-30}
            max={30}
            step={1}
            onValueChange={(v) => setAjusteEstacionalidad(Array.isArray(v) ? v[0] : v)}
          />
        </div>

        <div className="flex gap-2">
          <Button
            onClick={() => ejecutar({ idTitulo, tendencia: ajusteTendencia, estacionalidad: ajusteEstacionalidad })}
            disabled={cargando}
          >
            {cargando ? "Calculando…" : "Aplicar escenario"}
          </Button>
          <Button
            variant="secondary"
            onClick={() => {
              setAjusteTendencia(0);
              setAjusteEstacionalidad(0);
              ejecutar({ idTitulo, tendencia: 0, estacionalidad: 0 });
            }}
          >
            Restablecer
          </Button>
        </div>
      </div>

      <div className="rounded-xl border border-border bg-card p-4">
        <h3 className="mb-3 font-medium">Resultado del escenario</h3>
        {error && <p className="text-sm text-destructive">{error}</p>}
        {resultado && !error && (
          <div className="flex flex-col gap-3">
            <div>
              <div className="text-xs text-muted-foreground">Demanda proyectada</div>
              <div className="text-xl font-semibold">
                {resultado.demanda_proyectada.toLocaleString(undefined, { maximumFractionDigits: 0 })} unidades
              </div>
            </div>
            <div>
              <div className="text-xs text-muted-foreground">Tiraje recomendado</div>
              <div className="text-xl font-semibold">{resultado.tiraje_recomendado.toLocaleString()} unidades</div>
            </div>
            <div className="grid grid-cols-2 gap-3">
              <div>
                <div className="text-xs text-muted-foreground">Probabilidad de quiebre (estimada)</div>
                <div className="text-lg font-semibold">{resultado.prob_quiebre.toFixed(0)}%</div>
              </div>
              <div>
                <div className="text-xs text-muted-foreground">Probabilidad de sobrestock (estimada)</div>
                <div className="text-lg font-semibold">{resultado.prob_sobrestock.toFixed(0)}%</div>
              </div>
            </div>
            <div>
              <div className="mb-1 text-xs text-muted-foreground">Confianza del modelo</div>
              <Progress value={resultado.confianza_modelo} />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
