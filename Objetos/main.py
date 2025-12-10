from Objetos.circulo import Circulo
from Objetos.cuadrado import Cuadrado
from Objetos.elipse import Elipse
from Objetos.rectangulo import Rectangulo

def main():
    circulo = Circulo(radio=5, color="rojo")
    cuadrado = Cuadrado(lado=4, color="azul")
    elipse = Elipse(radio_mayor=6, radio_menor=3, color="amarillo")
    rectangulo = Rectangulo(ancho=8, alto=2, color="naranja")

    print(circulo)
    print(cuadrado)
    print(elipse)
    print(rectangulo)

if __name__ == "__main__":
    main()