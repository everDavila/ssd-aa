import { BookDetailTabs } from "@/components/book-detail-tabs";
import { TituloSelect } from "@/components/titulo-select";
import { getCatalogo, getCatalogoDetalle } from "@/lib/api";

export default async function PrediccionesPage({
  searchParams,
}: {
  searchParams: Promise<{ id?: string }>;
}) {
  const { id } = await searchParams;

  const lista = await getCatalogo({ pageSize: 100 });
  const conHistorial = lista.items.filter((item) => item.tiene_historial);
  const seleccionado = id && conHistorial.some((t) => t.id_titulo === id)
    ? id
    : conHistorial[0]?.id_titulo;

  const detalle = seleccionado ? await getCatalogoDetalle(seleccionado) : null;

  return (
    <div className="flex flex-col gap-4">
      <TituloSelect
        opciones={conHistorial.map((t) => ({ id_titulo: t.id_titulo, titulo: t.titulo }))}
        valor={seleccionado ?? ""}
      />
      {detalle ? <BookDetailTabs data={detalle} /> : (
        <p className="text-sm text-muted-foreground">No hay títulos con historial de ventas.</p>
      )}
    </div>
  );
}
