from entidad_arqueologica import (
    Lugar,
    Asentamiento,
    Enterramiento,
    AreaExplotacion,
    ConjuntoArqueologico,
    Dimension
)

def main():
    lugar1 = Lugar("Valle Antiguo", provincia="Provincia A", pais="Pais X")
    lugar2 = Lugar("Meseta Norte", provincia="Provincia B", pais="Pais X")

    sitio1 = Asentamiento("Asentamiento San Miguel", cronologia="Edad del Bronce", lugar=lugar1)
    sitio2 = Enterramiento("Enterramiento Las Lomas", cronologia="Edad del Hierro", lugar=lugar1)
    sitio3 = AreaExplotacion("Área de Explotación Río Seco", cronologia="Época Romana", lugar=lugar2)

    conjunto = ConjuntoArqueologico("Conjunto Valle Antiguo", cronologia="Neolítico", lugar=lugar1)
    conjunto.add_sitio(sitio1)
    conjunto.add_sitio(sitio2)

    d1 = Dimension("Superficie parcela", 1200.0, "m2")
    d2 = Dimension("Área excavada", 250.0, "m2")
    d3 = Dimension("Volumen estrato", 30.5, "m3")

    sitio1.add_dimension(d1)
    sitio1.add_dimension(d2)
    conjunto.add_dimension(d3)

    print(lugar1)
    for e in lugar1.entidades:
        print(" ", e)

    print()
    print(conjunto)
    print(" Sitios en conjunto:", conjunto.sitios)
    print()
    print("Dimensiones sitio1 totals:", sitio1.total_medida())
    print("Dimensiones conjunto totals:", conjunto.total_medida())

    print()
    print("Mover sitio3 a lugar1")
    sitio3.set_lugar(lugar1)
    print(lugar2)
    print(lugar1)

if __name__ == "__main__":
    main()