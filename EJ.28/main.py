from datetime import date
from objetos import (
    SitioArqueologico,
    Excavacion,
    ObjetoCompleto,
    FragmentoObjeto,
    Dimension,
    Material,
    Uso
)

def main():
    sitio = SitioArqueologico("S-001", "Yacimiento El Valle", ubicacion="Valle Antiguo")
    exc = Excavacion("EX-2025-01", fecha_inicio=date(2025, 5, 1))
    sitio.add_excavacion(exc)

    obj1 = ObjetoCompleto("OBJ-001", datacion="S. II", datacion_confianza=0.8, descripcion="Vasija completa", material=Material.CERAMICA, material_confianza=0.9)
    obj1.add_dimension(Dimension("altura", 14.5, "cm"))
    obj1.add_dimension(Dimension("diametro", 12.0, "cm"))
    obj1.add_uso(Uso("contenedor", fecha_inicio=date(10, 1, 1), fecha_fin=date(100, 1, 1)))

    frag1 = FragmentoObjeto("FRAG-001", parte_de=obj1, datacion="S. II", datacion_confianza=0.6, descripcion="Fragmento de borde", material=Material.CERAMICA)
    frag1.add_dimension(Dimension("peso", 0.025, "kg"))

    obj2 = ObjetoCompleto("OBJ-002", datacion="S. III", descripcion="Fragmentario reconstruido", material=Material.METAL)
    obj2.add_dimension(Dimension("longitud", 22.0, "cm"))

    obj1.add_similar(obj2)

    exc.add_objeto(obj1)
    exc.add_objeto(frag1)
    exc.add_objeto(obj2)

    print("Sitio, excavación y objetos encontrados:")
    print(sitio)
    print(exc)
    for o in exc.objetos:
        print(" ", o)

    print("\nSimilitudes:")
    print(obj1, "similares ->", obj1.similares)

    print("\nTotal medidas por unidad de OBJ-001:", obj1.total_medida_por_unidad())

    print("\nObjeto completo componentes:")
    print(obj1.componentes)

if __name__ == "__main__":
    main()