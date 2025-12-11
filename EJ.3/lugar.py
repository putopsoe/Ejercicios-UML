class Lugar:
    def __init__(self, institucion, ciudad, pais, titulo=None):
        self.institucion = institucion
        self.ciudad = ciudad
        self.pais = pais
        self.titulo = titulo
        self.obras = []

    def add_obra(self, cuadro):
        if cuadro not in self.obras:
            self.obras.append(cuadro)

    def __str__(self):
        obras_titles = ", ".join(f'"{o.titulo}"' for o in self.obras) if self.obras else "—"
        parts = [f'Lugar: {self.institucion} ({self.ciudad}, {self.pais})']
        if self.titulo:
            parts.append(f"TítuloLugar={self.titulo}")
        parts.append(f"Obras=[{obras_titles}]")
        return ", ".join(parts)