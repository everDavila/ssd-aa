"use client";

import { useRouter } from "next/navigation";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";

export function TituloSelect({
  opciones,
  valor,
}: {
  opciones: { id_titulo: string; titulo: string }[];
  valor: string;
}) {
  const router = useRouter();

  return (
    <Select value={valor} onValueChange={(id) => router.push(`/predicciones?id=${id}`)}>
      <SelectTrigger className="w-80">
        <SelectValue placeholder="Selecciona un título" />
      </SelectTrigger>
      <SelectContent>
        {opciones.map((op) => (
          <SelectItem key={op.id_titulo} value={op.id_titulo}>
            {op.titulo}
          </SelectItem>
        ))}
      </SelectContent>
    </Select>
  );
}
