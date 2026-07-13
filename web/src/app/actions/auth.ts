"use server";

import { redirect } from "next/navigation";
import { createSession, deleteSession } from "@/lib/session";

export type LoginState = { error?: string } | undefined;

export async function login(_prevState: LoginState, formData: FormData): Promise<LoginState> {
  const usuario = String(formData.get("usuario") ?? "");
  const contrasena = String(formData.get("contrasena") ?? "");

  const usuarioEsperado = process.env.SSD_AUTH_USER ?? "editor";
  const contrasenaEsperada = process.env.SSD_AUTH_PASSWORD ?? "ambar2026";

  if (usuario !== usuarioEsperado || contrasena !== contrasenaEsperada) {
    return { error: "Usuario o contraseña incorrectos." };
  }

  await createSession(usuario);
  redirect("/dashboard");
}

export async function logout() {
  await deleteSession();
  redirect("/login");
}
