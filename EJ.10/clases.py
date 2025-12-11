from datetime import date
from typing import Optional, List

class MiembroEquipo:
    def __init__(self, nombre: str, apellidos: str, roles: Optional[List[str]] = None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.roles = roles or []
        self.participa_en: List['Proyecto'] = []

    def add_rol(self, rol: str):
        if rol not in self.roles:
            self.roles.append(rol)

    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellidos}"

    def __str__(self):
        roles_str = ", ".join(self.roles) if self.roles else "Sin rol"
        proyectos_str = ", ".join(p.nombre for p in self.participa_en) if self.participa_en else "—"
        return f"{self.nombre_completo()} | Roles: {roles_str} | Proyectos: {proyectos_str}"


class LugarActuacion:
    def __init__(self, coordenada_x: float, coordenada_y: float, nombres: Optional[List[str]] = None):
        self.nombres = nombres or []
        self.coordenada_x = float(coordenada_x)
        self.coordenada_y = float(coordenada_y)
        self.proyectos: List['Proyecto'] = []

    def add_nombre(self, nombre: str):
        if nombre not in self.nombres:
            self.nombres.append(nombre)

    def __str__(self):
        nombres_str = ", ".join(self.nombres) if self.nombres else "Sin nombre"
        proyectos_str = ", ".join(p.nombre for p in self.proyectos) if self.proyectos else "—"
        return f"{nombres_str} ({self.coordenada_x}, {self.coordenada_y}) | Proyectos: {proyectos_str}"


class Proyecto:
    def __init__(self, nombre: str, fecha_inicio: date, fecha_fin: Optional[date] = None):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.miembros_equipo: List[MiembroEquipo] = []
        self.lugares_actuacion: List[LugarActuacion] = []

    def add_miembro(self, miembro: MiembroEquipo):
        if miembro not in self.miembros_equipo:
            self.miembros_equipo.append(miembro)
            if self not in miembro.participa_en:
                miembro.participa_en.append(self)

    def add_lugar(self, lugar: LugarActuacion):
        if lugar not in self.lugares_actuacion:
            self.lugares_actuacion.append(lugar)
            if self not in lugar.proyectos:
                lugar.proyectos.append(self)

    def estado(self) -> str:
        today = date.today()
        if today < self.fecha_inicio:
            return "No iniciado"
        elif self.fecha_fin and today > self.fecha_fin:
            return "Finalizado"
        else:
            return "En curso"

    def __str__(self):
        fecha_fin_str = self.fecha_fin.strftime("%d/%m/%Y") if self.fecha_fin else "—"
        partes = [
            f"Proyecto: {self.nombre}",
            f"Fecha: {self.fecha_inicio.strftime('%d/%m/%Y')} - {fecha_fin_str}",
            f"Estado: {self.estado()}",
            f"Miembros ({len(self.miembros_equipo)}):"
        ]
        for m in self.miembros_equipo:
            partes.append(f"  - {m.nombre_completo()} ({', '.join(m.roles) if m.roles else 'Sin rol'})")
        partes.append(f"Lugares ({len(self.lugares_actuacion)}):")
        for l in self.lugares_actuacion:
            nombres = ", ".join(l.nombres) if l.nombres else "Sin nombre"
            partes.append(f"  - {nombres} ({l.coordenada_x}, {l.coordenada_y})")
        return "\n".join(partes)