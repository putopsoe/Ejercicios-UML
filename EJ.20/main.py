from proyecto import Persona, Proyecto, Actuacion


def main():
    p_alice = Persona("Alice", identificador="P001")
    p_bob = Persona("Bob", identificador="P002")
    p_carol = Persona("Carol", identificador="P003")
    p_dan = Persona("Dan", identificador="P004")

    proyecto_a = Proyecto("Proyecto A")
    proyecto_b = Proyecto("Proyecto B")

    proyecto_a.add_responsable(p_alice, es_director=True)
    proyecto_a.add_responsable(p_bob)

    proyecto_b.add_responsable(p_bob, es_director=True)

    proyecto_a.add_tecnico(p_carol)
    proyecto_a.add_tecnico(p_dan)

    act1 = Actuacion("Excavación zona 1")
    act2 = Actuacion("Sondeo estrato 3")
    act3 = Actuacion("Estudio topográfico")

    proyecto_a.add_actuacion(act1)
    proyecto_a.add_actuacion(act2)
    proyecto_b.add_actuacion(act3)

    act1.add_tecnico(p_carol)
    act1.add_tecnico(p_dan)
    act2.add_tecnico(p_dan)
    act3.add_tecnico(p_carol)

    print("Proyectos y actuaciones:")
    print(proyecto_a)
    for a in proyecto_a.actuaciones:
        print(" ", a)

    print()
    print(proyecto_b)
    for a in proyecto_b.actuaciones:
        print(" ", a)

    print()
    print("Personas y roles:")
    personas = (p_alice, p_bob, p_carol, p_dan)
    for p in personas:
        print(p, "Roles:", p.roles_descripcion())

    print()
    print("Comprobaciones:")
    print(f"Alice es director de Proyecto A? ->", any(r for r in p_alice.roles if getattr(r, 'proyecto', None) is proyecto_a and isinstance(r, type(r)) and 'Responsable' in r.tipo()))
    print(f"Carol participa como técnico en Actuación 'Excavación zona 1'? ->", any(r for r in p_carol.roles if getattr(r, 'actuacion', None) is act1 and 'Técnico' in r.tipo()))


if __name__ == "__main__":
    main()