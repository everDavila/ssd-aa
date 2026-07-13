import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { ModelComparisonChart } from "@/components/charts/model-comparison-chart";
import { getModelos } from "@/lib/api";
import { cn } from "@/lib/utils";

export default async function ModelosPage() {
  const data = await getModelos();

  return (
    <div className="flex flex-col gap-4">
      <div className="overflow-hidden rounded-xl border border-border bg-card">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Modelo</TableHead>
              <TableHead>MAPE (%)</TableHead>
              <TableHead>MAE</TableHead>
              <TableHead>RMSE</TableHead>
              <TableHead>Tiempo de entrenamiento (s)</TableHead>
              <TableHead>Estado</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {data.filas.map((fila) => (
              <TableRow key={fila.modelo}>
                <TableCell className="font-medium">{fila.modelo}</TableCell>
                <TableCell>{fila.mape != null ? fila.mape.toFixed(2) : "—"}</TableCell>
                <TableCell>{fila.mae != null ? fila.mae.toFixed(2) : "—"}</TableCell>
                <TableCell>{fila.rmse != null ? fila.rmse.toFixed(2) : "—"}</TableCell>
                <TableCell>{fila.tiempo_entrenamiento_seg != null ? fila.tiempo_entrenamiento_seg.toFixed(3) : "—"}</TableCell>
                <TableCell>
                  <span
                    className={cn(
                      "rounded-full px-2.5 py-0.5 text-xs font-semibold",
                      fila.estado === "Activo" && "bg-emerald-100 text-emerald-700",
                      fila.estado === "Disponible" && "bg-secondary text-secondary-foreground",
                      fila.estado === "Próximamente" && "bg-amber-100 text-amber-700"
                    )}
                  >
                    {fila.estado === "Activo" ? "✅ Activo" : fila.estado === "Próximamente" ? "🚧 Próximamente" : fila.estado}
                  </span>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
      <p className="text-xs text-muted-foreground">
        LSTM requiere TensorFlow y ventanas de secuencia por título; se deja fuera de
        este MVP porque, con el volumen real de datos disponible, no hay evidencia
        de que supere a los 3 modelos ya entrenados aquí.
      </p>

      <Card>
        <CardHeader>
          <CardTitle>MAPE por modelo (menor es mejor)</CardTitle>
        </CardHeader>
        <CardContent>
          <ModelComparisonChart data={data.filas} />
        </CardContent>
      </Card>

      <div className="rounded-xl border border-border bg-card p-4 text-sm">
        Modelo activo: <span className="font-semibold">{data.modelo_activo}</span> — menor MAPE de
        prueba entre los evaluados.
      </div>
    </div>
  );
}
