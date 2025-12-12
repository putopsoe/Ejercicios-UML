from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import List, Optional
from enum import Enum


class Material(Enum):
    CERAMICA = "Cerámica"
    METAL = "Metal"
    PIEDRA = "Piedra"
    HUESO = "Hueso"
    ORGANICO = "Orgánico"
    OTRO = "Otro"


@dataclass
class Dimension:
    nombre: str
    medida: float
    unidad: str

    def __repr__(self):
        return f"Dimension(nombre={self.nombre}, medida={self.medida}, unidad={self.unidad})"


class SitioArqueologico:
    def __init__(self, codigo: str, nombre: str, ubicacion: Optional[str] = None):
        self.codigo = str(codigo)
        self.nombre = str(nombre)
        self.ubicacion = str(ubicacion) if ubicacion else ""
        self.excavaciones: List[Excavacion] = []

    def add_excavacion(self, excavacion: "Excavacion"):
        if excavacion not in self.excavaciones:
            self.excavaciones.append(excavacion)
            excavacion.sitio = self

    def __repr__(self):
        return f"SitioArqueologico(codigo={self.codigo}, nombre={self.nombre}, excavaciones={len(self.excavaciones)})"


class Excavacion:
    def __init__(self, referencia: str, fecha_inicio: date, fecha_fin: Optional[date] = None):
        self.referencia = str(referencia)
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.sitio: Optional[SitioArqueologico] = None
        self.objetos: List[ObjetoArqueologico] = []

    def add_objeto(self, obj: "ObjetoArqueologico"):
        if obj not in self.objetos:
            self.objetos.append(obj)
            obj.excavacion = self

    def remove_objeto(self, obj: "ObjetoArqueologico"):
        if obj in self.objetos:
            self.objetos.remove(obj)
            obj.excavacion = None

    def objetos_completos(self) -> List["ObjetoCompleto"]:
        return [o for o in self.objetos if isinstance(o, ObjetoCompleto)]

    def objetos_fragmentos(self) -> List["FragmentoObjeto"]:
        return [o for o in self.objetos if isinstance(o, FragmentoObjeto)]

    def __repr__(self):
        sitio = self.sitio.codigo if self.sitio else "-"
        return f"Excavacion(ref={self.referencia}, sitio={sitio}, objetos={len(self.objetos)})"


class Uso:
    def __init__(self, descripcion: str, fecha_inicio: Optional[date] = None, fecha_fin: Optional[date] = None):
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def __repr__(self):
        fstr = f"{self.fecha_inicio.isoformat() if self.fecha_inicio else '?'}"
        fstr += f" - {self.fecha_fin.isoformat() if self.fecha_fin else 'en curso'}"
        return f"Uso({self.descripcion}, {fstr})"


class ObjetoArqueologico:
    def __init__(
        self,
        codigo: str,
        datacion: Optional[str] = None,
        datacion_confianza: Optional[float] = None,
        descripcion: Optional[str] = None,
        material: Optional[Material] = None,
        material_confianza: Optional[float] = None
    ):
        self.codigo = str(codigo)
        self.datacion = str(datacion) if datacion else ""
        self.datacion_confianza = float(datacion_confianza) if datacion_confianza is not None else None
        self.descripcion = str(descripcion) if descripcion else ""
        self.material = material
        self.material_confianza = float(material_confianza) if material_confianza is not None else None
        self.dimensiones: List[Dimension] = []
        self.excavacion: Optional[Excavacion] = None
        self.observaciones: Optional[str] = None
        self.similares: List["ObjetoArqueologico"] = []

    def add_dimension(self, d: Dimension):
        if d not in self.dimensiones:
            self.dimensiones.append(d)

    def add_similar(self, otro: "ObjetoArqueologico"):
        if otro is self:
            return
        if otro not in self.similares:
            self.similares.append(otro)
            otro.add_similar(self)

    def remove_similar(self, otro: "ObjetoArqueologico"):
        if otro in self.similares:
            self.similares.remove(otro)
            if self in otro.similares:
                otro.similares.remove(self)

    def total_medida_por_unidad(self) -> dict:
        totals = {}
        for d in self.dimensiones:
            totals.setdefault(d.unidad, 0.0)
            totals[d.unidad] += d.medida
        return totals

    def __repr__(self):
        mat = self.material.value if self.material else "desconocido"
        return f"Objeto(codigo={self.codigo}, material={mat}, datacion={self.datacion}, dimensiones={len(self.dimensiones)})"


class ObjetoCompleto(ObjetoArqueologico):
    def __init__(self, codigo: str, datacion: Optional[str] = None, datacion_confianza: Optional[float] = None,
                 descripcion: Optional[str] = None, material: Optional[Material] = None, material_confianza: Optional[float] = None):
        super().__init__(codigo, datacion, datacion_confianza, descripcion, material, material_confianza)
        self.usos: List[Uso] = []
        self.componentes: List[ObjetoArqueologico] = []

    def add_uso(self, uso: Uso):
        if uso not in self.usos:
            self.usos.append(uso)

    def add_componente(self, componente: ObjetoArqueologico):
        if componente not in self.componentes:
            self.componentes.append(componente)

    def __repr__(self):
        base = super().__repr__()
        return f"{base[:-1]}, completo, componentes={len(self.componentes)})"


class FragmentoObjeto(ObjetoArqueologico):
    def __init__(self, codigo: str, parte_de: Optional[ObjetoCompleto] = None, datacion: Optional[str] = None,
                 datacion_confianza: Optional[float] = None, descripcion: Optional[str] = None, material: Optional[Material] = None,
                 material_confianza: Optional[float] = None):
        super().__init__(codigo, datacion, datacion_confianza, descripcion, material, material_confianza)
        self.parte_de: Optional[ObjetoCompleto] = None
        if parte_de is not None:
            self.set_parte_de(parte_de)

    def set_parte_de(self, obj: ObjetoCompleto):
        if self.parte_de is obj:
            return
        if self.parte_de:
            if self in self.parte_de.componentes:
                self.parte_de.componentes.remove(self)
        self.parte_de = obj
        if obj and self not in obj.componentes:
            obj.add_componente(self)

    def __repr__(self):
        parte = self.parte_de.codigo if self.parte_de else "sin referencia"
        return f"Fragmento(codigo={self.codigo}, parte_de={parte})"