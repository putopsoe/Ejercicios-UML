class Figura:
    """Clase base para todas las figuras con atributo común 'color'."""
    def __init__(self, color: str = "negro"):
        self.color = color

    def __str__(self):
        return f"{self.__class__.__name__}(color={self.color})"