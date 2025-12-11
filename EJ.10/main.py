from datetime import date
from clases import Proyecto, MiembroEquipo, LugarActuacion

def main():
    # Miembros
    ana = MiembroEquipo("Ana", "García López", roles=["Jefe de Proyecto"])
    carlos = MiembroEquipo("Carlos", "Martínez Pérez", roles=["Desarrollador", "Tester"])
    maria = MiembroEquipo("María", "Rodríguez Silva", roles=["Desarrolladora", "Analista"])
    juan = MiembroEquipo("Juan", "López Fernández", roles=["Diseñador"])

    # Lugares
    madrid = LugarActuacion(40.4168, -3.7038, nombres=["Oficina Madrid", "Sede Principal"])
    barcelona = LugarActuacion(41.3851, 2.1734, nombres=["Oficina Barcelona"])
    remoto = LugarActuacion(0.0, 0.0, nombres=["Trabajo Remoto"])

    # Proyectos
    p1 = Proyecto("Sistema de Gestión", date(2024, 1, 15), date(2025, 6, 30))
    p2 = Proyecto("Portal Web", date(2024, 6, 1), date(2025, 12, 31))

    # Asociar miembros a proyectos
    p1.add_miembro(ana)
    p1.add_miembro(carlos)
    p1.add_miembro(maria)
    p2.add_miembro(ana)
    p2.add_miembro(juan)
    p2.add_miembro(maria)

    # Asociar lugares a proyectos
    p1.add_lugar(madrid)
    p1.add_lugar(remoto)
    p2.add_lugar(barcelona)
    p2.add_lugar(madrid)

    # Mostrar
    print("="*70)
    print("PROYECTOS")
    print("="*70)
    for p in (p1, p2):
        print(p)
        print()

    print("="*70)
    print("MIEMBROS")
    print("="*70)
    for m in (ana, carlos, maria, juan):
        print(f"MiembroEquipo: {m}")
    print()

    print("="*70)
    print("LUGARES")
    print("="*70)
    for l in (madrid, barcelona, remoto):
        print(f"LugarActuacion: {l}")
    print()

if __name__ == "__main__":
    main()