from figura import Figura
from elipse import Elipse
from circulo import Circulo
from cuadrado import Cuadrado
from rectangulo import Rectangulo

def main():
    # Crear instancias (objetos)
    e = Elipse(eje_mayor=10, eje_menor=6, color="rojo")
    c = Circulo(diametro=5, color="azul")
    cu = Cuadrado(longitud=4, color="verde")
    r = Rectangulo(longitud=6, anchura=3, color="amarillo")

    figuras = (e, c, cu, r)

    # Imprimir objetos y atributos
    for obj in figuras:
        print(obj)
        print("  Atributos:", vars(obj))
        print(f"  Es instancia de {obj.__class__.__name__}? ->", isinstance(obj, obj.__class__))
        print(f"  Es instancia de Figura? ->", isinstance(obj, Figura))
        print()

    # Ejemplos de relaciones claras (instanciación)
    print("Comprobaciones rápidas de tipo:")
    print(" - 'e' es Elipse y Figura:", isinstance(e, Elipse), isinstance(e, Figura))
    print(" - 'c' es Circulo y Figura:", isinstance(c, Circulo), isinstance(c, Figura))
    print(" - 'cu' es Cuadrado y Figura:", isinstance(cu, Cuadrado), isinstance(cu, Figura))
    print(" - 'r' es Rectangulo y Figura:", isinstance(r, Rectangulo), isinstance(r, Figura))

if __name__ == '__main__':
    main()