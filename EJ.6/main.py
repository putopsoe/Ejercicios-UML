from datetime import date
from persona import Persona

def main():
    # Crear instancias de Persona
    p1 = Persona(
        nombre="Juan",
        primer_apellido="García",
        segundo_apellido="López",
        fecha_nacimiento=date(1990, 5, 15),
        sexo="Hombre",
        numero_identificacion="12345678A"
    )

    p2 = Persona(
        nombre="María",
        primer_apellido="Rodríguez",
        fecha_nacimiento=date(1985, 8, 22),
        sexo="Mujer",
        numero_identificacion="87654321B"
    )

    p3 = Persona(
        nombre="Carlos",
        primer_apellido="Martínez",
        segundo_apellido="Pérez",
        fecha_nacimiento=date(2000, 3, 10),
        sexo="Hombre"
        # sin número de identificación
    )

    personas = (p1, p2, p3)

    # Imprimir personas y sus atributos
    for i, persona in enumerate(personas, 1):
        print(f"Persona {i}:")
        print(f"  {persona}")
        print(f"  Nombre completo: {persona.nombre_completo()}")
        print(f"  Atributos: {vars(persona)}")
        print(f"  Es instancia de Persona? -> {isinstance(persona, Persona)}")
        print()

if __name__ == "__main__":
    main()