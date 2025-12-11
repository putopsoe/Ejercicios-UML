class Cuadro:
    def __init__(self, titulo, ac=None, tecnica=None, sub_tecnica=None, soporte=None,
                 autor=None, estado_conservacion=None):
        self.titulo = titulo
        self.ac = ac
        self.tecnica = tecnica
        self.sub_tecnica = sub_tecnica
        self.soporte = soporte
        self.autor = autor
        self.estado_conservacion = estado_conservacion
        self.lugar = None
        self.replicado_de = None

    def set_location(self, lugar):
        self.lugar = lugar
        if hasattr(lugar, "add_obra"):
            lugar.add_obra(self)

    def set_replica_of(self, original):
        self.replicado_de = original

    def __str__(self):
        parts = [f'"{self.titulo}"']
        if self.autor:
            parts.append(f"Autor={self.autor}")
        if self.ac:
            parts.append(f"AC={self.ac}")
        if self.tecnica:
            parts.append(f"Técnica={self.tecnica}")
        if self.sub_tecnica:
            parts.append(f"Sub-técnica={self.sub_tecnica}")
        if self.soporte:
            parts.append(f"Soporte={self.soporte}")
        if self.estado_conservacion:
            parts.append(f"Estado={self.estado_conservacion}")
        if self.replicado_de:
            parts.append(f'Replica_de="{self.replicado_de.titulo}"')
        if self.lugar:
            parts.append(f'Ubicado_en="{self.lugar.institucion}, {self.lugar.ciudad}, {self.lugar.pais}"')
        return ", ".join(parts)