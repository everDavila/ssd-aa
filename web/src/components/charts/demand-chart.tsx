"use client";

import { CartesianGrid, Line, LineChart, XAxis, YAxis } from "recharts";
import {
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
  type ChartConfig,
} from "@/components/ui/chart";
import { formatMonth } from "@/lib/format";
import type { SeriePunto } from "@/lib/types";

const chartConfig: ChartConfig = {
  ventas: { label: "Ventas reales", color: "var(--chart-1)" },
};

export function DemandChart({ data }: { data: SeriePunto[] }) {
  return (
    <ChartContainer config={chartConfig} className="aspect-auto h-72 w-full">
      <LineChart data={data} margin={{ left: 4, right: 12, top: 8, bottom: 0 }}>
        <CartesianGrid vertical={false} />
        <XAxis dataKey="fecha" tickFormatter={formatMonth} tickLine={false} axisLine={false} />
        <YAxis tickLine={false} axisLine={false} width={40} />
        <ChartTooltip content={<ChartTooltipContent labelFormatter={(label) => formatMonth(String(label))} />} />
        <Line
          type="monotone"
          dataKey="ventas"
          stroke="var(--color-ventas)"
          strokeWidth={2}
          dot={{ r: 3 }}
        />
      </LineChart>
    </ChartContainer>
  );
}
