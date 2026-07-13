import { ScenarioSimulator } from "@/components/scenario-simulator";
import { getCatalogo, simulateScenario } from "@/lib/api";

export default async function SimuladorPage({
  searchParams,
}: {
  searchParams: Promise<{ id?: string }>;
}) {
  const { id } = await searchParams;
  const lista = await getCatalogo({ pageSize: 100 });
  const conHistorial = lista.items.filter((item) => item.tiene_historial);
  const idInicial = id && conHistorial.some((t) => t.id_titulo === id) ? id : conHistorial[0]?.id_titulo;

  const resultadoInicial = idInicial
    ? await simulateScenario({ id_titulo: idInicial, ajuste_tendencia: 0, ajuste_estacionalidad: 0 })
    : null;

  return (
    <div className="flex flex-col gap-4">
      <p className="text-sm text-muted-foreground">
        El mockup original usaba variables ilustrativas (campaña escolar, publicidad,
        precio, competencia) que no existen en los datos reales. Este simulador ajusta
        las palancas que el modelo sí controla: la tendencia reciente de ventas y un
        factor de estacionalidad aplicado sobre el pronóstico.
      </p>
      {idInicial ? (
        <ScenarioSimulator
          opciones={conHistorial.map((t) => ({ id_titulo: t.id_titulo, titulo: t.titulo }))}
          idTituloInicial={idInicial}
          resultadoInicial={resultadoInicial}
        />
      ) : (
        <p className="text-sm text-muted-foreground">No hay títulos con historial de ventas.</p>
      )}
    </div>
  );
}
