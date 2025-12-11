from datetime import date
from typing import Optional, List
from enums import Tecnica, SubTecnica, Material, EstadoConservacion

class Cuadro:
    """
    Atributos:
    - titulos: lista de textos (0..* títulos)
    - cronologia: date (1)
    - tecnica: Tecnica enum (1)
    - sub_tecnica: SubTecnica enum (1)
    - material: Material enum (1)
    - autor: texto (1)
    - estado_conservacion: EstadoConservacion enum (1)
    - ubicacion: texto (ubicación actual)
    - tiene_copias: bool
    """
    def __init__(self, cronologia: date, tecnica: Tecnica, sub_tecnica: SubTecnica,
                 material: Material, autor: str, estado_conservacion: EstadoConservacion,
                 titulos: Optional[List[str]] = None, ubicacion: Optional[str] = None,
                 tiene_copias: bool = False):
        self.titulos = titulos or []
        self.cronologia = cronologia
        self.tecnica = tecnica
        self.sub_tecnica = sub_tecnica
        self.material = material
        self.autor = autor
        self.estado_conservacion = estado_conservacion
        self.ubicacion = ubicacion
        self.tiene_copias = tiene_copias

    def add_titulo(self, titulo: str):
        """Añade un título si no existe ya."""
        if titulo not in self.titulos:
            self.titulos.append(titulo)

    def titulo_principal(self) -> str:
        """Devuelve el primer título o 'Sin título'."""
        return self.titulos[0] if self.titulos else "Sin título"

    def __str__(self):
        titulos_str = ", ".join(f'"{t}"' for t in self.titulos) if self.titulos else "Sin título"
        copias = "Sí" if self.tiene_copias else "No"
        ubicacion_str = self.ubicacion or "Ubicación desconocida"
        
        partes = [
            f"Títulos: {titulos_str}",
            f"Cronología: {self.cronologia.strftime('%Y')}",
            f"Autor: {self.autor}",
            f"Técnica: {self.tecnica.value}",
            f"Sub-técnica: {self.sub_tecnica.value}",
            f"Material del soporte: {self.material.value}",
            f"Estado de conservación: {self.estado_conservacion.value}",
            f"Ubicación actual: {ubicacion_str}",
            f"¿Existen copias? {copias}"
        ]
        return "\n  ".join(partes)