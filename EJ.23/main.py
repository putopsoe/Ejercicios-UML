from construccion import Edificio, ConjuntoConstruido


def print_structure(node, indent: int = 0):
    spacer = "  " * indent
    print(spacer + repr(node))
    if not node.is_leaf():
        for child in node.children():
            print_structure(child, indent + 1)


def main():
    conjunto_principal = ConjuntoConstruido("C-ROOT", "Conjunto Urbano Principal")

    e1 = Edificio("E-001", "Casa Sol", numero="1", plantas=3)
    e2 = Edificio("E-002", "Casa Luna", numero="2", plantas=2)
    e3 = Edificio("E-003", "Torre Norte", numero="10", plantas=8)

    barrio_norte = ConjuntoConstruido("C-01", "Barrio Norte")
    barrio_sur = ConjuntoConstruido("C-02", "Barrio Sur")

    e4 = Edificio("E-004", "Residencia Olivo", numero="5A", plantas=4)
    e5 = Edificio("E-005", "Edificio Central", numero="12", plantas=6)

    barrio_norte.add_child(e1)
    barrio_norte.add_child(e2)
    barrio_norte.add_child(e3)

    barrio_sur.add_child(e4)
    barrio_sur.add_child(e5)

    conjunto_principal.add_child(barrio_norte)
    conjunto_principal.add_child(barrio_sur)

    print("Estructura completa:")
    print_structure(conjunto_principal)

    print()
    print("Resumen:")
    print("Total de edificios en conjunto_principal:", conjunto_principal.count_edificios())
    print("Listado de edificios:")
    for ed in conjunto_principal.list_edificios():
        print(" -", ed)

    print()
    print("Mover e3 a barrio_sur")
    barrio_norte.remove_child(e3)
    barrio_sur.add_child(e3)

    print()
    print("Estructura actualizada:")
    print_structure(conjunto_principal)
    print("Total de edificios actualizado:", conjunto_principal.count_edificios())


if __name__ == "__main__":
    main()