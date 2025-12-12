from __future__ import annotations
from enum import Enum
from typing import List, Optional


class TipoSitio(Enum):
    ASENTAMIENTO = "Asentamiento"
    ENTERRAMIENTO = "Enterramiento"
    AREA_EXPLOTACION = "Área de explotación"


class Dimension:
    def __init__(self, nombre: str, medida: float, unidad: str):
        self.nombre = str(nombre)
        self.medida = float(medida)
        self.unidad = str(unidad)

    def __repr__(self):
        return f"Dimension(nombre={self.nombre}, medida={self.medida}, unidad={self.unidad})"


class Lugar:
    def __init__(self, nombre: str, provincia: Optional[str] = None, pais: Optional[str] = None):
        self.nombre = str(nombre)
        self.provincia = provincia or ""
        self.pais = pais or ""
        self.entidades: List[EntidadArqueologica] = []

    def add_entidad(self, entidad: "EntidadArqueologica"):
        if entidad not in self.entidades:
            self.entidades.append(entidad)
            entidad.lugar = self

    def remove_entidad(self, entidad: "EntidadArqueologica"):
        if entidad in self.entidades:
            self.entidades.remove(entidad)
            if entidad.lugar is self:
                entidad.lugar = None

    def __repr__(self):
        return f"Lugar(nombre={self.nombre}, provincia={self.provincia}, pais={self.pais}, entidades={len(self.entidades)})"


class EntidadArqueologica:
    def __init__(self, nombre: str, cronologia: Optional[str] = None, lugar: Optional[Lugar] = None):
        self.nombre = str(nombre)
        self.cronologia = str(cronologia) if cronologia is not None else ""
        self.lugar: Optional[Lugar] = None
        self.dimensiones: List[Dimension] = []
        if lugar is not None:
            lugar.add_entidad(self)

    def add_dimension(self, dimension: Dimension):
        if dimension not in self.dimensiones:
            self.dimensiones.append(dimension)

    def remove_dimension(self, dimension: Dimension):
        if dimension in self.dimensiones:
            self.dimensiones.remove(dimension)

    def total_medida(self) -> dict:
        totals = {}
        for d in self.dimensiones:
            totals.setdefault(d.unidad, 0.0)
            totals[d.unidad] += d.medida
        return totals

    def set_lugar(self, lugar: Optional[Lugar]):
        if self.lugar is lugar:
            return
        if self.lugar:
            self.lugar.remove_entidad(self)
        if lugar:
            lugar.add_entidad(self)

    def __repr__(self):
        lugar_name = self.lugar.nombre if self.lugar else "sin lugar"
        dims = len(self.dimensiones)
        return f"EntidadArqueologica(nombre={self.nombre}, cronologia={self.cronologia}, lugar={lugar_name}, dimensiones={dims})"


class SitioArqueologico(EntidadArqueologica):
    def __init__(self, nombre: str, tipo: TipoSitio, cronologia: Optional[str] = None, lugar: Optional[Lugar] = None):
        super().__init__(nombre, cronologia=cronologia, lugar=lugar)
        self.tipo = tipo

    def __repr__(self):
        return f"SitioArqueologico(nombre={self.nombre}, tipo={self.tipo.value}, cronologia={self.cronologia}, lugar={self.lugar.nombre if self.lugar else 'sin lugar'})"


class Asentamiento(SitioArqueologico):
    def __init__(self, nombre: str, cronologia: Optional[str] = None, lugar: Optional[Lugar] = None):
        super().__init__(nombre, tipo=TipoSitio.ASENTAMIENTO, cronologia=cronologia, lugar=lugar)


class Enterramiento(SitioArqueologico):
    def __init__(self, nombre: str, cronologia: Optional[str] = None, lugar: Optional[Lugar] = None):
        super().__init__(nombre, tipo=TipoSitio.ENTERRAMIENTO, cronologia=cronologia, lugar=lugar)


class AreaExplotacion(SitioArqueologico):
    def __init__(self, nombre: str, cronologia: Optional[str] = None, lugar: Optional[Lugar] = None):
        super().__init__(nombre, tipo=TipoSitio.AREA_EXPLOTACION, cronologia=cronologia, lugar=lugar)


class ConjuntoArqueologico(EntidadArqueologica):
    def __init__(self, nombre: str, cronologia: Optional[str] = None, lugar: Optional[Lugar] = None):
        super().__init__(nombre, cronologia=cronologia, lugar=lugar)
        self.sitios: List[SitioArqueologico] = []

    def add_sitio(self, sitio: SitioArqueologico):
        if sitio not in self.sitios:
            self.sitios.append(sitio)

    def remove_sitio(self, sitio: SitioArqueologico):
        if sitio in self.sitios:
            self.sitios.remove(sitio)

    def sitios_count(self) -> int:
        return len(self.sitios)

    def __repr__(self):
        lugar_name = self.lugar.nombre if self.lugar else "sin lugar"
        return f"ConjuntoArqueologico(nombre={self.nombre}, cronologia={self.cronologia}, lugar={lugar_name}, sitios={len(self.sitios)})"