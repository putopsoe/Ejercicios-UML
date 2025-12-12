from typing import List, Optional


class Persona:
    """
    nombre: str
    identificador: Optional[str]
    roles: List[Rol]
    """
    def __init__(self, nombre: str, identificador: Optional[str] = None):
        self.nombre = nombre
        self.identificador = identificador
        self.roles: List['Rol'] = []

    def __repr__(self):
        if self.identificador:
            return f"Persona({self.nombre}, id={self.identificador})"
        return f"Persona({self.nombre})"

    def roles_descripcion(self) -> List[str]:
        return [r.descripcion() for r in self.roles]


class Rol:
    """
    Tipo base para roles asociados a una persona. Puede estar asociado a un proyecto y/o a una actuación.
    """
    def __init__(self, persona: Persona, proyecto: Optional['Proyecto'] = None, actuacion: Optional['Actuacion'] = None):
        self.persona = persona
        self.proyecto = proyecto
        self.actuacion = actuacion
        persona.roles.append(self)

    def tipo(self) -> str:
        return "Rol"

    def descripcion(self) -> str:
        if self.proyecto and self.actuacion:
            return f"{self.tipo()} en Proyecto='{self.proyecto.nombre}' / Actuación='{self.actuacion.nombre}'"
        if self.proyecto:
            return f"{self.tipo()} en Proyecto='{self.proyecto.nombre}'"
        if self.actuacion:
            return f"{self.tipo()} en Actuación='{self.actuacion.nombre}'"
        return self.tipo()


class Responsable(Rol):
    """
    Rol de responsable. Un responsable puede dirigir (director) un proyecto.
    """
    def __init__(self, persona: Persona, proyecto: Optional['Proyecto'] = None, es_director: bool = False):
        super().__init__(persona, proyecto=proyecto, actuacion=None)
        self.es_director = es_director

    def tipo(self) -> str:
        return "Responsable (Director)" if self.es_director else "Responsable"

    def descripcion(self) -> str:
        desc = super().descripcion()
        if self.es_director:
            desc = desc + " - Director"
        return desc


class Tecnico(Rol):
    """
    Rol de técnico. Puede participar en proyectos y en actuaciones.
    """
    def __init__(self, persona: Persona, proyecto: Optional['Proyecto'] = None, actuacion: Optional['Actuacion'] = None):
        super().__init__(persona, proyecto=proyecto, actuacion=actuacion)

    def tipo(self) -> str:
        return "Técnico"


class Proyecto:
    """
    Proyecto arqueológico, compuesto por varias actuaciones concretas.
    """
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.actuaciones: List['Actuacion'] = []
        self.responsables: List[Responsable] = []
        self.tecnicos: List[Tecnico] = []
        self.director: Optional[Responsable] = None

    def add_responsable(self, persona: Persona, es_director: bool = False) -> Responsable:
        existing = [r for r in self.responsables if r.persona is persona]
        if existing:
            r = existing[0]
            if es_director:
                r.es_director = True
                self.director = r
            return r
        r = Responsable(persona, proyecto=self, es_director=es_director)
        self.responsables.append(r)
        if es_director:
            self.director = r
        return r

    def add_tecnico(self, persona: Persona) -> Tecnico:
        existing = [t for t in self.tecnicos if t.persona is persona]
        if existing:
            return existing[0]
        t = Tecnico(persona, proyecto=self, actuacion=None)
        self.tecnicos.append(t)
        return t

    def add_actuacion(self, act: 'Actuacion'):
        if act not in self.actuaciones:
            self.actuaciones.append(act)
            act.proyecto = self

    def __repr__(self):
        d = self.director.persona.nombre if self.director else "Sin director"
        return f"Proyecto({self.nombre}, director={d}, actuaciones={len(self.actuaciones)})"


class Actuacion:
    """
    Actuación concreta dentro de un proyecto.
    """
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.proyecto: Optional[Proyecto] = None
        self.tecnicos: List[Tecnico] = []

    def add_tecnico(self, persona: Persona) -> Tecnico:
        existing = [t for t in self.tecnicos if t.persona is persona]
        if existing:
            return existing[0]
        t = Tecnico(persona, proyecto=self.proyecto, actuacion=self)
        self.tecnicos.append(t)
        if self.proyecto and persona and not any(t0.persona is persona for t0 in self.proyecto.tecnicos):
            self.proyecto.add_tecnico(persona)
        return t

    def __repr__(self):
        return f"Actuacion({self.nombre}, proyecto={self.proyecto.nombre if self.proyecto else 'None'}, tecnicos={len(self.tecnicos)})"