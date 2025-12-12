from datetime import date, timedelta
from biblioteca import Biblioteca, Planta, Tematica, Libro, Ejemplar, Lector, Empleado

def main():
    b = Biblioteca("Biblioteca Municipal", "C/ Mayor, 1", "900-123-456", 8, 1996)

    p1 = Planta(1, 1000)
    p2 = Planta(2, 1200)
    p3 = Planta(3, 900)
    b.add_planta(p1)
    b.add_planta(p2)
    b.add_planta(p3)

    t_infantil = Tematica("Infantil")
    t_narrativa = Tematica("Narrativa")
    t_ensayo = Tematica("Ensayo")
    p1.add_tematica(t_infantil)
    p2.add_tematica(t_narrativa)
    p3.add_tematica(t_ensayo)

    libro1 = Libro("978-000x", "Cuentos para niños", 2012, "Español")
    e1 = Ejemplar("E001", "Primera", 2012)
    e2 = Ejemplar("E002", "Segunda", 2018)
    libro1.add_ejemplar(e1)
    libro1.add_ejemplar(e2)

    libro2 = Libro("978-111x", "Narrativa Actual", 2010, "Español")
    e3 = Ejemplar("E003", "Beta", 2010)
    libro2.add_ejemplar(e3)

    libro3 = Libro("978-222x", "Ensayo Moderno", 2015, "Español")
    e4 = Ejemplar("E004", "Gama", 2015)
    libro3.add_ejemplar(e4)

    t_infantil.add_libro(libro1)
    t_narrativa.add_libro(libro2)
    t_ensayo.add_libro(libro3)

    lector1 = Lector("Juan Pérez", "L-123", "C/ Falsa 1")
    empleado1 = Empleado("Ana Gómez", "E-001", "C/ Real 5", "EMP-01")
    b.register_lector(lector1)
    b.register_empleado(empleado1)

    prest1 = b.prestar_ejemplar(e1, lector_id="L-123")
    print("Préstamo 1:", prest1)
    prest2 = b.prestar_ejemplar(e3, lector_id="L-123")
    print("Préstamo 2:", prest2)

    fecha_inicio_pasada = date.today() - timedelta(days=40)
    prest_pasado = b.prestar_ejemplar(e2, lector_id="L-123", fecha_inicio=fecha_inicio_pasada, dias=30)
    print("Préstamo pasado (para forzar retraso):", prest_pasado)
    if prest_pasado:
        print("Dias retraso:", prest_pasado.dias_retraso())

    prest_empleado = b.prestar_ejemplar(e4, lector_id="E-001", empleado_codigo="EMP-01")
    print("Préstamo por empleado:", prest_empleado)

    b.devolver_ejemplar(e2, fecha_devolucion=date.today())
    print("Después de devolver e2:", prest_pasado)

    print("\nEstado Biblioteca y ejemplares:")
    print(b)
    for lib in (libro1, libro2, libro3):
        print(lib)
        for ej in lib.ejemplares:
            print(" ", ej)

if __name__ == "__main__":
    main()