import { ArrowDown, ArrowUp } from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { cn } from "@/lib/utils";

type KpiCardProps = {
  label: string;
  value: string;
  delta?: string;
  deltaDirection?: "up" | "down";
  deltaTone?: "good" | "bad";
};

export function KpiCard({ label, value, delta, deltaDirection, deltaTone = "good" }: KpiCardProps) {
  const Icon = deltaDirection === "up" ? ArrowUp : ArrowDown;
  return (
    <Card>
      <CardContent className="flex flex-col gap-1 py-2">
        <span className="text-sm text-muted-foreground">{label}</span>
        <span className="text-2xl font-semibold text-card-foreground">{value}</span>
        {delta && (
          <span
            className={cn(
              "flex items-center gap-1 text-xs font-medium",
              deltaTone === "good" ? "text-emerald-600" : "text-red-600"
            )}
          >
            <Icon size={12} />
            {delta}
          </span>
        )}
      </CardContent>
    </Card>
  );
}
