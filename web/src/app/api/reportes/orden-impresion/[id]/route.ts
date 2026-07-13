import { NextResponse } from "next/server";

const BASE_URL = process.env.SSD_API_BASE_URL ?? "http://127.0.0.1:8000";

export async function GET(_req: Request, ctx: RouteContext<"/api/reportes/orden-impresion/[id]">) {
  const { id } = await ctx.params;
  const upstream = await fetch(`${BASE_URL}/api/reportes/orden-impresion/${encodeURIComponent(id)}.csv`, {
    cache: "no-store",
  });

  if (!upstream.ok) {
    return NextResponse.json({ error: "Título no encontrado" }, { status: upstream.status });
  }

  return new NextResponse(upstream.body, {
    headers: {
      "Content-Type": "text/csv",
      "Content-Disposition": upstream.headers.get("content-disposition") ?? `attachment; filename="orden_${id}.csv"`,
    },
  });
}
