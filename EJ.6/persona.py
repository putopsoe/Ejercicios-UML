from datetime import date
from typing import Optional

class Persona:
    """
    Atributos:
    - nombre: texto (obligatorio)
    - primer_apellido: texto (obligatorio)
    - segundo_apellido: texto (opcional, 0..1)
    - fecha_nacimiento: date (obligatorio)
    - sexo: texto (obligatorio)
    - numero_identificacion: texto (opcional, 0..1)
    """
    def __init__(self, nombre: str, primer_apellido: str, fecha_nacimiento: date,
                 sexo: str, segundo_apellido: Optional[str] = None,
                 numero_identificacion: Optional[str] = None):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.numero_identificacion = numero_identificacion

    def nombre_completo(self) -> str:
        """Retorna el nombre completo de la persona."""
        apellidos = self.primer_apellido
        if self.segundo_apellido:
            apellidos += f" {self.segundo_apellido}"
        return f"{self.nombre} {apellidos}"

    def edad(self) -> int:
        """Calcula la edad actual de la persona."""
        today = date.today()
        return today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )

    def __str__(self):
        parts = [
            f"Nombre: {self.nombre}",
            f"Primer apellido: {self.primer_apellido}",
            f"Segundo apellido: {self.segundo_apellido or '—'}",
            f"Fecha de nacimiento: {self.fecha_nacimiento.strftime('%d/%m/%Y')}",
            f"Edad: {self.edad()}",
            f"Sexo: {self.sexo}",
            f"Número de identificación: {self.numero_identificacion or '—'}"
        ]
        return "\n  ".join(parts)