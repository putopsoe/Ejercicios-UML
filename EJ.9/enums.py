from enum import Enum

class Tecnica(Enum):
    ACUARELA = "Acuarela"
    OLEO = "Óleo"
    PASTEL = "Pastel"
    FRESCO = "Fresco"

class SubTecnica(Enum):
    SFUMATO = "Sfumato"
    PINCELADA_SIMPLE = "Pincelada simple"
    COLLAGE = "Collage"
    VELADURA = "Veladura"

class Material(Enum):
    MADERA = "Madera"
    ALAMO = "Álamo"
    NOGAL = "Nogal"
    LIENZO = "Lienzo"

class EstadoConservacion(Enum):
    EXCELENTE = "Excelente"
    BUENO = "Bueno"
    REGULAR = "Regular"
    MALO = "Malo"
    DESTRUIDO = "Destruido"