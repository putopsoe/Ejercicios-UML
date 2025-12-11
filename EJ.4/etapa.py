class EtapaConstruccion:
    def __init__(self, nombre, fecha_inicio=None, fecha_fin=None):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def __str__(self):
        fin = self.fecha_fin if self.fecha_fin is not None else "nulo"
        return f"{self.nombre}: {self.fecha_inicio} - {fin}"