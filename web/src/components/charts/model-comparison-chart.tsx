"use client";

import { Bar, BarChart, CartesianGrid, Cell, XAxis, YAxis } from "recharts";
import { ChartContainer, ChartTooltip, ChartTooltipContent, type ChartConfig } from "@/components/ui/chart";
import type { ModeloItem } from "@/lib/types";

const chartConfig: ChartConfig = {
  mape: { label: "MAPE (%)", color: "var(--chart-1)" },
};

export function ModelComparisonChart({ data }: { data: ModeloItem[] }) {
  const conDatos = data.filter((item) => item.mape != null);
  return (
    <ChartContainer config={chartConfig} className="aspect-auto h-64 w-full">
      <BarChart data={conDatos} margin={{ left: 4, right: 12, top: 8, bottom: 0 }}>
        <CartesianGrid vertical={false} />
        <XAxis dataKey="modelo" tickLine={false} axisLine={false} />
        <YAxis tickLine={false} axisLine={false} width={40} />
        <ChartTooltip content={<ChartTooltipContent />} />
        <Bar dataKey="mape" radius={4}>
          {conDatos.map((item) => (
            <Cell key={item.modelo} fill={item.estado === "Activo" ? "var(--chart-1)" : "#c4b5fd"} />
          ))}
        </Bar>
      </BarChart>
    </ChartContainer>
  );
}
