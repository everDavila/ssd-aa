"use client";

import { usePathname } from "next/navigation";
import { LogOut, User } from "lucide-react";
import { pageTitle } from "@/lib/nav";
import { logout } from "@/app/actions/auth";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

export function AppTopbar() {
  const pathname = usePathname();

  return (
    <header className="flex items-center justify-between border-b border-border bg-background/80 px-6 py-4 backdrop-blur">
      <span className="rounded-full bg-primary px-4 py-1.5 text-sm font-semibold text-primary-foreground">
        {pageTitle(pathname)}
      </span>

      <div className="flex items-center gap-4">
        <div className="hidden rounded-lg border border-border bg-card px-3 py-1.5 text-sm text-muted-foreground sm:block">
          Campaña: Escolar 2026
        </div>

        <DropdownMenu>
          <DropdownMenuTrigger className="flex items-center gap-2 rounded-lg px-2 py-1.5 hover:bg-accent">
            <Avatar className="size-8">
              <AvatarFallback className="bg-secondary text-secondary-foreground">
                <User size={16} />
              </AvatarFallback>
            </Avatar>
            <div className="hidden text-left text-xs leading-tight sm:block">
              <div className="font-medium text-foreground">Planificador</div>
              <div className="text-muted-foreground">Administrador</div>
            </div>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuGroup>
              <DropdownMenuLabel>Planificador · Administrador</DropdownMenuLabel>
              <DropdownMenuSeparator />
              <DropdownMenuItem variant="destructive" onClick={() => logout()}>
                <LogOut size={14} /> Cerrar sesión
              </DropdownMenuItem>
            </DropdownMenuGroup>
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
    </header>
  );
}
