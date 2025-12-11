from figura import Figura
from typing import Optional
import math

class Elipse(Figura):
    """
    Atributos:
    - eje_mayor: número (mayor diámetro)
    - eje_menor: número (menor diámetro)
    - longitud: número (perímetro aproximado) — opcional
    - color: texto (heredado)
    """
    def __init__(self, eje_mayor: float, eje_menor: float, longitud: Optional[float] = None, color: str = "negro"):
        super().__init__(color=color)
        self.eje_mayor = float(eje_mayor)
        self.eje_menor = float(eje_menor)
        # si no se proporciona, calculamos una aproximación de la circunferencia (Ramanujan)
        if longitud is None:
            a = self.eje_mayor / 2
            b = self.eje_menor / 2
            # aproximación de Ramanujan
            h = ((a - b)**2) / ((a + b)**2) if (a + b) != 0 else 0
            self.longitud = math.pi * (a + b) * (1 + (3*h) / (10 + math.sqrt(4 - 3*h)))
        else:
            self.longitud = float(longitud)

    def __str__(self):
        return (f"Elipse(eje_mayor={self.eje_mayor}, eje_menor={self.eje_menor}, "
                f"longitud={self.longitud:.3f}, color={self.color})")