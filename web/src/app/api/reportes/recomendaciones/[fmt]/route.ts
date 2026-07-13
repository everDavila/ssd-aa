import { NextResponse } from "next/server";

const BASE_URL = process.env.SSD_API_BASE_URL ?? "http://127.0.0.1:8000";
const CONTENT_TYPES: Record<string, string> = {
  csv: "text/csv",
  xlsx: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
};

export async function GET(_req: Request, ctx: RouteContext<"/api/reportes/recomendaciones/[fmt]">) {
  const { fmt } = await ctx.params;
  if (fmt !== "csv" && fmt !== "xlsx") {
    return NextResponse.json({ error: "Formato no soportado" }, { status: 400 });
  }

  const upstream = await fetch(`${BASE_URL}/api/reportes/recomendaciones.${fmt}`, { cache: "no-store" });
  if (!upstream.ok) {
    return NextResponse.json({ error: "No se pudo generar el reporte" }, { status: upstream.status });
  }

  return new NextResponse(upstream.body, {
    headers: {
      "Content-Type": CONTENT_TYPES[fmt],
      "Content-Disposition":
        upstream.headers.get("content-disposition") ?? `attachment; filename="recomendaciones_tiraje.${fmt}"`,
    },
  });
}
