from datetime import date
from enum import Enum
from typing import Optional

class TipoActuacion(Enum):
    SONDEO = "Sondeo"
    EXCAVACION = "Excavación"
    SEGUIMIENTO = "Seguimiento"

class ActuacionArqueologica:
    """
    Atributos:
    - fecha_inicio: date (1)
    - fecha_fin: Optional[date] (0..1)
    - tipo: TipoActuacion (1)
    """
    def __init__(self, fecha_inicio: date, tipo: TipoActuacion, fecha_fin: Optional[date] = None):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tipo = tipo

    def duracion_dias(self) -> Optional[int]:
        """Devuelve la duración en días si existe fecha_fin, o None si está en curso."""
        if self.fecha_fin is None:
            return None
        return (self.fecha_fin - self.fecha_inicio).days

    def __str__(self):
        fin = self.fecha_fin.strftime("%d/%m/%Y") if self.fecha_fin else "—"
        dur = self.duracion_dias()
        dur_str = f"{dur} días" if dur is not None else "en curso"
        return f"Actuación({self.tipo.value}): {self.fecha_inicio.strftime('%d/%m/%Y')} - {fin} ({dur_str})"