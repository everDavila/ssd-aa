import { cn } from "@/lib/utils";

export type RiskLevel = "Bajo" | "Medio" | "Alto";

const STYLES: Record<RiskLevel, string> = {
  Bajo: "bg-emerald-100 text-emerald-700",
  Medio: "bg-amber-100 text-amber-700",
  Alto: "bg-red-100 text-red-700",
};

const DOT: Record<RiskLevel, string> = {
  Bajo: "bg-emerald-500",
  Medio: "bg-amber-500",
  Alto: "bg-red-500",
};

export function RiskBadge({ nivel, className }: { nivel: RiskLevel; className?: string }) {
  return (
    <span
      className={cn(
        "inline-flex items-center gap-1.5 rounded-full px-2.5 py-0.5 text-xs font-semibold",
        STYLES[nivel],
        className
      )}
    >
      <span className={cn("size-1.5 rounded-full", DOT[nivel])} />
      {nivel}
    </span>
  );
}
