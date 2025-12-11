class Edificio:
    def __init__(self, nombre, culto=None, fecha_inicio_construccion=None,
                 fecha_fin_construccion=None, fecha_primera_consagracion=None,
                 fecha_inicio_segunda_etapa=None, fecha_segunda_consagracion=None,
                 fecha_declaracion_bic=None, material=None, estilos=None):
        self.nombre = nombre
        self.culto = culto
        self.fecha_inicio_construccion = fecha_inicio_construccion
        self.fecha_fin_construccion = fecha_fin_construccion
        self.fecha_primera_consagracion = fecha_primera_consagracion
        self.fecha_inicio_segunda_etapa = fecha_inicio_segunda_etapa
        self.fecha_segunda_consagracion = fecha_segunda_consagracion
        self.fecha_declaracion_bic = fecha_declaracion_bic
        self.material = material
        self.estilos = estilos or []
        self.lugar = None
        self.etapas = []

    def add_etapa(self, etapa):
        if etapa not in self.etapas:
            self.etapas.append(etapa)

    def set_lugar(self, lugar):
        if lugar:
            lugar.add_edificio(self)

    def __str__(self):
        estilos = ", ".join(self.estilos) if self.estilos else "—"
        partes = [
            f"Nombre: {self.nombre}",
            f"Culto: {self.culto or '—'}",
            f"Construcción: {self.fecha_inicio_construccion or '—'} - {self.fecha_fin_construccion or '—'}",
            f"Primera consagración: {self.fecha_primera_consagracion or '—'}",
            f"Inicio segunda etapa: {self.fecha_inicio_segunda_etapa or '—'}",
            f"Segunda consagración: {self.fecha_segunda_consagracion or '—'}",
            f"Declaración BIC: {self.fecha_declaracion_bic or '—'}",
            f"Material: {self.material or '—'}",
            f"Estilos: {estilos}"
        ]
        if self.lugar:
            partes.append(f"Ubicación: {self.lugar.institucion if hasattr(self.lugar, 'institucion') else (self.lugar.titulo or '')} {self.lugar.ciudad}, {self.lugar.comunidad or ''}, {self.lugar.pais or ''}".strip())
        if self.etapas:
            partes.append("Etapas:")
            for e in self.etapas:
                partes.append(f"  - {e}")
        return "\n".join(partes)