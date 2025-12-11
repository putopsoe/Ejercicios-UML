from figura import Figura

class Rectangulo(Figura):
    """
    Atributos:
    - longitud: número (alto)
    - anchura: número (ancho)
    - color: texto (heredado)
    """
    def __init__(self, longitud: float, anchura: float, color: str = "negro"):
        super().__init__(color=color)
        self.longitud = float(longitud)
        self.anchura = float(anchura)

    def __str__(self):
        return f"Rectangulo(longitud={self.longitud}, anchura={self.anchura}, color={self.color})"