from figura import Figura

class Circulo(Figura):
    """
    Atributos:
    - diametro: número
    - color: texto (heredado)
    """
    def __init__(self, diametro: float, color: str = "negro"):
        super().__init__(color=color)
        self.diametro = float(diametro)

    @property
    def radio(self):
        return self.diametro / 2

    def __str__(self):
        return f"Circulo(diametro={self.diametro}, radio={self.radio}, color={self.color})"