from datetime import date, timedelta
from typing import List, Optional


class Biblioteca:
    def __init__(self, nombre: str, direccion: str, telefono: str, numero_empleados: int, ano_apertura: int):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.numero_empleados = numero_empleados
        self.ano_apertura = ano_apertura
        self.plantas: List[Planta] = []
        self.lectores: dict[str, Lector] = {}
        self.empleados: dict[str, Empleado] = {}
        self.prestamos: List[Prestamo] = []

    def add_planta(self, planta: "Planta"):
        if planta not in self.plantas:
            self.plantas.append(planta)
            planta.biblioteca = self

    def register_lector(self, lector: "Lector"):
        self.lectores[lector.numero_identificacion] = lector

    def register_empleado(self, empleado: "Empleado"):
        self.empleados[empleado.codigo] = empleado
        self.register_lector(empleado)

    def prestar_ejemplar(self, ejemplar: "Ejemplar", lector_id: str, empleado_codigo: Optional[str] = None,
                        dias: Optional[int] = None, fecha_inicio: Optional[date] = None) -> Optional["Prestamo"]:
        if ejemplar.prestamo_actual is not None:
            return None
        lector = self.lectores.get(lector_id)
        if lector is None:
            return None
        empleado = None
        if empleado_codigo:
            empleado = self.empleados.get(empleado_codigo)
        if fecha_inicio is None:
            fecha_inicio = date.today()
        if dias is None:
            dias = 30 if not isinstance(lector, Empleado) else 60
        prestamo = Prestamo(lector, ejemplar, empleado, fecha_inicio, fecha_inicio + timedelta(days=dias))
        ejemplar.prestamo_actual = prestamo
        lector.prestamos.append(prestamo)
        if empleado:
            empleado.prestamos.append(prestamo)
        self.prestamos.append(prestamo)
        return prestamo

    def devolver_ejemplar(self, ejemplar: "Ejemplar", fecha_devolucion: Optional[date] = None) -> Optional["Prestamo"]:
        prestamo = ejemplar.prestamo_actual
        if prestamo is None:
            return None
        if fecha_devolucion is None:
            fecha_devolucion = date.today()
        prestamo.fecha_real_devolucion = fecha_devolucion
        ejemplar.prestamo_actual = None
        return prestamo

    def capacidad_total(self) -> int:
        s = 0
        for p in self.plantas:
            s += p.capacidad
        return s

    def __repr__(self):
        return f"{self.nombre} ({self.direccion}) - Plantas: {len(self.plantas)} - Empleados: {self.numero_empleados}"


class Planta:
    def __init__(self, numero: int, capacidad: int):
        self.numero = numero
        self.capacidad = capacidad
        self.tematicas: List[Tematica] = []
        self.biblioteca: Optional[Biblioteca] = None

    def add_tematica(self, t: "Tematica"):
        if t not in self.tematicas:
            self.tematicas.append(t)
            t.planta = self

    def __repr__(self):
        return f"Planta {self.numero} (capacidad={self.capacidad})"


class Tematica:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros: List[Libro] = []
        self.planta: Optional[Planta] = None

    def add_libro(self, libro: "Libro"):
        if libro not in self.libros:
            self.libros.append(libro)
            libro.tematicas.append(self)

    def __repr__(self):
        return f"Temática: {self.nombre} - Libros: {len(self.libros)}"


class Libro:
    def __init__(self, isbn: str, titulo: str, ano_publicacion: int, idioma: str):
        self.isbn = isbn
        self.titulo = titulo
        self.ano_publicacion = ano_publicacion
        self.idioma = idioma
        self.ejemplares: List[Ejemplar] = []
        self.tematicas: List[Tematica] = []

    def add_ejemplar(self, ejemplar: "Ejemplar"):
        if ejemplar not in self.ejemplares:
            ejemplar.libro = self
            self.ejemplares.append(ejemplar)

    def ejemplares_disponibles(self) -> List["Ejemplar"]:
        return [e for e in self.ejemplares if e.is_disponible()]

    def __repr__(self):
        return f"{self.titulo} (ISBN={self.isbn}) - Ejemplares: {len(self.ejemplares)}"


class Ejemplar:
    def __init__(self, codigo: str, editorial: str, ano_adquisicion: int):
        self.codigo = codigo
        self.editorial = editorial
        self.ano_adquisicion = ano_adquisicion
        self.libro: Optional[Libro] = None
        self.prestamo_actual: Optional[Prestamo] = None

    def is_disponible(self) -> bool:
        return self.prestamo_actual is None

    def __repr__(self):
        libro = self.libro.titulo if self.libro else "sin libro"
        estado = "disponible" if self.is_disponible() else "prestado"
        return f"Ejemplar {self.codigo} - {libro} ({estado})"


class Lector:
    def __init__(self, nombre: str, numero_identificacion: str, direccion: str):
        self.nombre = nombre
        self.numero_identificacion = numero_identificacion
        self.direccion = direccion
        self.prestamos: List[Prestamo] = []

    def activo(self) -> bool:
        return True

    def __repr__(self):
        return f"Lector {self.nombre} ({self.numero_identificacion})"


class Empleado(Lector):
    def __init__(self, nombre: str, numero_identificacion: str, direccion: str, codigo: str):
        super().__init__(nombre, numero_identificacion, direccion)
        self.codigo = codigo

    def __repr__(self):
        return f"Empleado {self.nombre} (cod={self.codigo})"


class Prestamo:
    def __init__(self, lector: Lector, ejemplar: Ejemplar, empleado: Optional[Empleado], fecha_inicio: date,
                 fecha_estipulada_devolucion: date):
        self.lector = lector
        self.ejemplar = ejemplar
        self.empleado = empleado
        self.fecha_inicio = fecha_inicio
        self.fecha_estipulada_devolucion = fecha_estipulada_devolucion
        self.fecha_real_devolucion: Optional[date] = None

    def dias_retraso(self, hoy: Optional[date] = None) -> int:
        if hoy is None:
            hoy = date.today()
        compare = self.fecha_real_devolucion if self.fecha_real_devolucion else hoy
        retraso = (compare - self.fecha_estipulada_devolucion).days
        return retraso if retraso > 0 else 0

    def esta_vencido(self, hoy: Optional[date] = None) -> bool:
        return self.dias_retraso(hoy) > 0

    def __repr__(self):
        estado = "devuelto" if self.fecha_real_devolucion else "en préstamo"
        empleado = self.empleado.codigo if self.empleado else "-"
        return (f"Préstamo [{estado}] Ejemplar={self.ejemplar.codigo} Lector={self.lector.numero_identificacion} "
                f"Empleado={empleado} Inicio={self.fecha_inicio} Estipulada={self.fecha_estipulada_devolucion} "
                f"Real={self.fecha_real_devolucion}")