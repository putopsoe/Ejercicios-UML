from datetime import date
from enums import Material
from estructura import Estructura

def main():
    # Estructura principal
    e1 = Estructura("E1", datacion=date(1100,1,1), materiales=[Material.PIEDRA, Material.GRANITO])
    # Subestructuras
    s1 = Estructura("E1.1", datacion=date(1120,1,1), materiales=[Material.LADRILLO])
    s2 = Estructura("E1.2", materiales=[Material.MADERA, Material.CERAMICA])
    # Añadir subestructuras a la estructura marco
    e1.add_subestructura(s1)
    e1.add_subestructura(s2)

    # Añadir material adicional
    s2.add_material(Material.ADOBE)

    # Mostrar
    for obj in (e1, s1, s2):
        print(obj)
        print("  dict:", obj.to_dict())
        print()

if __name__ == "__main__":
    main()