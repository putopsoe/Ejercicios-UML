from __future__ import annotations
from typing import List, Optional


class Construccion:
    """
    Componente base del patrón Composite para representaciones de construcciones.
    Puede contener subconstrucciones (ConjuntoConstruido o Edificio).
    """
    def __init__(self, codigo: str, nombre: str):
        self.codigo = str(codigo)
        self.nombre = str(nombre)
        self.parent: Optional['Construccion'] = None

    def add_child(self, child: 'Construccion'):
        raise NotImplementedError

    def remove_child(self, child: 'Construccion'):
        raise NotImplementedError

    def children(self) -> List['Construccion']:
        return []

    def is_leaf(self) -> bool:
        return False

    def count_edificios(self) -> int:
        return 0

    def list_edificios(self) -> List['Edificio']:
        return []

    def __repr__(self):
        return f"{self.__class__.__name__}(codigo={self.codigo}, nombre={self.nombre})"


class Edificio(Construccion):
    """
    Hoja del patrón Composite que representa un Edificio.
    """
    def __init__(self, codigo: str, nombre: str, numero: Optional[str] = None, plantas: Optional[int] = 1):
        super().__init__(codigo, nombre)
        self.numero = str(numero) if numero is not None else None
        self.plantas = int(plantas) if plantas is not None else 1

    def is_leaf(self) -> bool:
        return True

    def count_edificios(self) -> int:
        return 1

    def list_edificios(self) -> List['Edificio']:
        return [self]

    def __repr__(self):
        n = f", numero={self.numero}" if self.numero else ""
        p = f", plantas={self.plantas}" if self.plantas is not None else ""
        return f"Edificio(codigo={self.codigo}, nombre={self.nombre}{n}{p})"


class ConjuntoConstruido(Construccion):
    """
    Composite que agrupa múltiples Construcciones (Edificios o Conjuntos).
    """
    def __init__(self, codigo: str, nombre: str):
        super().__init__(codigo, nombre)
        self._children: List[Construccion] = []

    def add_child(self, child: Construccion):
        if child not in self._children:
            self._children.append(child)
            child.parent = self

    def remove_child(self, child: Construccion):
        if child in self._children:
            self._children.remove(child)
            child.parent = None

    def children(self) -> List[Construccion]:
        return list(self._children)

    def is_leaf(self) -> bool:
        return False

    def count_edificios(self) -> int:
        total = 0
        for c in self._children:
            total += c.count_edificios()
        return total

    def list_edificios(self) -> List['Edificio']:
        eds: List[Edificio] = []
        for c in self._children:
            eds.extend(c.list_edificios())
        return eds

    def __repr__(self):
        return f"ConjuntoConstruido(codigo={self.codigo}, nombre={self.nombre}, children={len(self._children)})"