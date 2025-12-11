from cuadro import Cuadro
from lugar import Lugar

def main():
    # Obra original (La Gioconda)
    gioconda = Cuadro(
        titulo="La Gioconda",
        ac="1503 - 1516",
        tecnica="Óleo",
        sub_tecnica="Sfumato",
        soporte="Madera de álamo",
        autor="Leonardo da Vinci",
        estado_conservacion="Regular"
    )
    l1 = Lugar(institucion="Museo del Louvre", ciudad="París", pais="Francia", titulo="La Gioconda")
    gioconda.set_location(l1)

    # Réplica (El Prado)
    replica = Cuadro(
        titulo="Gioconda de El Prado",
        ac="1503 - 1516",
        tecnica="Óleo",
        sub_tecnica="Pincelada simple",
        soporte="Madera de nogal",
        autor="Anónimo",
        estado_conservacion="Bueno"
    )
    l2 = Lugar(institucion="Museo del Prado", ciudad="Madrid", pais="España", titulo="Gioconda de El Prado")
    replica.set_location(l2)
    replica.set_replica_of(gioconda)

    # Mostrar
    for obj in (gioconda, replica, l1, l2):
        print(obj)
        print()

if __name__ == "__main__":
    main()