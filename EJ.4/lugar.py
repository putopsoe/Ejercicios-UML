class Lugar:
    def __init__(self, ciudad, comunidad=None, pais=None, titulo=None):
        self.titulo = titulo
        self.ciudad = ciudad
        self.comunidad = comunidad
        self.pais = pais
        self.edificios = []

    def add_edificio(self, edificio):
        if edificio not in self.edificios:
            self.edificios.append(edificio)
            edificio.lugar = self

    def __str__(self):
        titulo = f"{self.titulo} - " if self.titulo else ""
        loc = f"{titulo}{self.ciudad}, {self.comunidad or '—'}, {self.pais or '—'}"
        edifics = ", ".join(e.nombre for e in self.edificios) if self.edificios else "—"
        return f"Lugar: {loc}\nEdificios: [{edifics}]"