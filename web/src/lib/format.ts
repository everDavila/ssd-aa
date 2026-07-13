const MESES_CORTOS = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"];

export function formatMonth(fechaIso: string): string {
  const fecha = new Date(fechaIso);
  return `${MESES_CORTOS[fecha.getUTCMonth()]} ${String(fecha.getUTCFullYear()).slice(2)}`;
}
