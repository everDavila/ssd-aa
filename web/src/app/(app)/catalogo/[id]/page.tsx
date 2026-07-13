import { notFound } from "next/navigation";
import { BookDetailTabs } from "@/components/book-detail-tabs";
import { getCatalogoDetalle } from "@/lib/api";

export default async function DetalleLibroPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const data = await getCatalogoDetalle(id);
  if (!data) notFound();

  return <BookDetailTabs data={data} />;
}
