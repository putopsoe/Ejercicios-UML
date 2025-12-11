from figura import Figura

class Cuadrado(Figura):
    """
    Atributos:
    - longitud: número (longitud del lado)
    - color: texto (heredado)
    """
    def __init__(self, longitud: float, color: str = "negro"):
        super().__init__(color=color)
        self.longitud = float(longitud)

    def __str__(self):
        return f"Cuadrado(longitud={self.longitud}, color={self.color})"