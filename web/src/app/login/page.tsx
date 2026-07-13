import { Library, Sprout } from "lucide-react";
import { LoginForm } from "@/components/login-form";

const LIBROS = [
  { color: "#4C2FD1", ancho: "w-40" },
  { color: "#6D4FF2", ancho: "w-44" },
  { color: "#A78BFA", ancho: "w-36" },
  { color: "#EEE9FE", ancho: "w-48" },
  { color: "#8B5CF6", ancho: "w-40" },
];

export default function LoginPage() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-background p-6">
      <div className="grid w-full max-w-4xl grid-cols-1 items-center gap-10 md:grid-cols-2">
        <div className="hidden flex-col items-center justify-center gap-6 md:flex">
          <div className="flex flex-col-reverse items-center gap-1">
            {LIBROS.map((libro, i) => (
              <div
                key={i}
                className={`h-6 ${libro.ancho} rounded-sm shadow-sm`}
                style={{ backgroundColor: libro.color }}
              />
            ))}
          </div>
          <Sprout className="text-emerald-600" size={40} />
        </div>

        <div className="rounded-2xl bg-card p-8 shadow-lg">
          <div className="mb-6 flex items-center gap-3">
            <div className="flex size-11 items-center justify-center rounded-xl bg-primary text-primary-foreground">
              <Library size={22} />
            </div>
            <div>
              <h1 className="text-lg font-semibold text-card-foreground">SSD Editorial</h1>
              <p className="text-sm text-muted-foreground">
                Sistema de Soporte a Decisiones
                <br />
                Predicción de Demanda Bibliográfica
              </p>
            </div>
          </div>

          <LoginForm />
        </div>

        <p className="col-span-full text-center text-xs text-muted-foreground">
          © 2026 Editorial — Todos los derechos reservados
        </p>
      </div>
    </div>
  );
}
