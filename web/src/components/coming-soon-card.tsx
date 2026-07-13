import { Card, CardContent } from "@/components/ui/card";

export function ComingSoonCard({ children }: { children?: React.ReactNode }) {
  return (
    <Card>
      <CardContent className="py-10 text-center text-muted-foreground">
        {children ?? "Esta sección se conecta a datos reales en la Fase 1b/2."}
      </CardContent>
    </Card>
  );
}
