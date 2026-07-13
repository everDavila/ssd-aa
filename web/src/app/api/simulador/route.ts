import { NextResponse } from "next/server";

const BASE_URL = process.env.SSD_API_BASE_URL ?? "http://127.0.0.1:8000";

export async function POST(req: Request) {
  const body = await req.json();
  const upstream = await fetch(`${BASE_URL}/api/simulador`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
    cache: "no-store",
  });

  const data = await upstream.json();
  return NextResponse.json(data, { status: upstream.status });
}
