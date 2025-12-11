from datetime import date
from typing import Optional, List
from enums import Material

class Estructura:
    """
    Clase que representa una estructura arqueológica.
    Atributos:
     - codigo: str (1)
     - datacion: Optional[date] (0..1)
     - materiales: List[Material] (1..*)
    Asociaciones:
     - estructura_marco: Optional[Estructura] (0..1)  -- parent/reference
     - subestructuras: List[Estructura] (0..*)         -- hijos
    """
    def __init__(self, codigo: str, datacion: Optional[date] = None, materiales: Optional[List[Material]] = None):
        if not codigo:
            raise ValueError("El código es obligatorio.")
        self.codigo = codigo
        self.datacion = datacion
        self.materiales: List[Material] = materiales or []
        self.subestructuras: List["Estructura"] = []
        self.estructura_marco: Optional["Estructura"] = None

    def add_material(self, material: Material):
        if material not in self.materiales:
            self.materiales.append(material)

    def add_subestructura(self, sub: "Estructura"):
        if sub is self:
            raise ValueError("Una estructura no puede ser subestructura de sí misma.")
        if sub not in self.subestructuras:
            # desvincular de un padre anterior si existiera
            if sub.estructura_marco and sub.estructura_marco is not self:
                try:
                    sub.estructura_marco.subestructuras.remove(sub)
                except ValueError:
                    pass
            sub.estructura_marco = self
            self.subestructuras.append(sub)

    def remove_subestructura(self, sub: "Estructura"):
        if sub in self.subestructuras:
            self.subestructuras.remove(sub)
            sub.estructura_marco = None

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "datacion": self.datacion.isoformat() if isinstance(self.datacion, date) else None,
            "materiales": [m.value for m in self.materiales],
            "estructura_marco": self.estructura_marco.codigo if self.estructura_marco else None,
            "subestructuras": [s.codigo for s in self.subestructuras]
        }

    def __str__(self):
        dat = self.datacion.year if isinstance(self.datacion, date) else (self.datacion or "—")
        mats = ", ".join(m.value for m in self.materiales) if self.materiales else "—"
        parent = self.estructura_marco.codigo if self.estructura_marco else "—"
        subs = ", ".join(s.codigo for s in self.subestructuras) if self.subestructuras else "—"
        return (f"Estructura(codigo={self.codigo}, datacion={dat}, materiales=[{mats}], "
                f"estructura_marco={parent}, subestructuras=[{subs}])")