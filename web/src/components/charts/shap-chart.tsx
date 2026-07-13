"use client";

import { Bar, BarChart, CartesianGrid, Cell, XAxis, YAxis } from "recharts";
import { ChartContainer, ChartTooltip, ChartTooltipContent, type ChartConfig } from "@/components/ui/chart";
import type { FactorImpacto } from "@/lib/types";

const chartConfig: ChartConfig = {
  impacto: { label: "Impacto" },
};

export function ShapChart({ data }: { data: FactorImpacto[] }) {
  const ordenado = [...data].sort((a, b) => a.impacto - b.impacto);
  return (
    <ChartContainer config={chartConfig} className="aspect-auto h-72 w-full">
      <BarChart data={ordenado} layout="vertical" margin={{ left: 24, right: 24, top: 8, bottom: 8 }}>
        <CartesianGrid horizontal={false} />
        <XAxis type="number" tickLine={false} axisLine={false} />
        <YAxis
          type="category"
          dataKey="factor"
          tickLine={false}
          axisLine={false}
          width={180}
          tick={{ fontSize: 12 }}
        />
        <ChartTooltip content={<ChartTooltipContent />} />
        <Bar dataKey="impacto" radius={4}>
          {ordenado.map((item, index) => (
            <Cell key={index} fill={item.impacto < 0 ? "#ef4444" : "var(--chart-1)"} />
          ))}
        </Bar>
      </BarChart>
    </ChartContainer>
  );
}
