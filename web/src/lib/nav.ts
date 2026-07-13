import {
  LayoutDashboard,
  BookOpen,
  TrendingUp,
  Bell,
  Bot,
  SlidersHorizontal,
  FileText,
  type LucideIcon,
} from "lucide-react";

export type NavItem = {
  href: string;
  label: string;
  icon: LucideIcon;
};

export const NAV_ITEMS: NavItem[] = [
  { href: "/dashboard", label: "Dashboard", icon: LayoutDashboard },
  { href: "/catalogo", label: "Catálogo de Libros", icon: BookOpen },
  { href: "/predicciones", label: "Predicciones", icon: TrendingUp },
  { href: "/alertas", label: "Alertas", icon: Bell },
  { href: "/modelos", label: "Modelos IA", icon: Bot },
  { href: "/simulador", label: "Simulador", icon: SlidersHorizontal },
  { href: "/reportes", label: "Reportes y Configuración", icon: FileText },
];

export function pageTitle(pathname: string): string {
  const item = NAV_ITEMS.find(
    (i) => pathname === i.href || pathname.startsWith(`${i.href}/`)
  );
  return item?.label ?? "SSD Editorial";
}
