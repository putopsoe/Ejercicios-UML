from datetime import date
from cuadro import Cuadro
from enums import Tecnica, SubTecnica, Material, EstadoConservacion

def main():
    # La Gioconda (Leonardo da Vinci)
    gioconda = Cuadro(
        titulos=["La Gioconda", "Mona Lisa"],
        cronologia=date(1503, 1, 1),
        tecnica=Tecnica.OLEO,
        sub_tecnica=SubTecnica.SFUMATO,
        material=Material.ALAMO,
        autor="Leonardo da Vinci",
        estado_conservacion=EstadoConservacion.REGULAR,
        ubicacion="Museo del Louvre, París",
        tiene_copias=True
    )

    # Las Meninas (Diego Velázquez)
    meninas = Cuadro(
        titulos=["Las Meninas"],
        cronologia=date(1656, 1, 1),
        tecnica=Tecnica.OLEO,
        sub_tecnica=SubTecnica.PINCELADA_SIMPLE,
        material=Material.LIENZO,
        autor="Diego Velázquez",
        estado_conservacion=EstadoConservacion.BUENO,
        ubicacion="Museo del Prado, Madrid",
        tiene_copias=False
    )

    # La Noche Estrellada (Vincent van Gogh)
    noche_estrellada = Cuadro(
        titulos=["La Noche Estrellada"],
        cronologia=date(1889, 1, 1),
        tecnica=Tecnica.OLEO,
        sub_tecnica=SubTecnica.PINCELADA_SIMPLE,
        material=Material.LIENZO,
        autor="Vincent van Gogh",
        estado_conservacion=EstadoConservacion.BUENO,
        ubicacion="Museum of Modern Art (MoMA), Nueva York",
        tiene_copias=False
    )

    # El Grito (Edvard Munch)
    grito = Cuadro(
        titulos=["El Grito"],
        cronologia=date(1893, 1, 1),
        tecnica=Tecnica.OLEO,
        sub_tecnica=SubTecnica.PINCELADA_SIMPLE,
        material=Material.LIENZO,
        autor="Edvard Munch",
        estado_conservacion=EstadoConservacion.REGULAR,
        ubicacion="Galería Nacional de Noruega, Oslo",
        tiene_copias=True
    )

    cuadros = (gioconda, meninas, noche_estrellada, grito)

    for cuadro in cuadros:
        print(f"Cuadro: {cuadro.titulo_principal()}")
        print(f"  {cuadro}")
        print(f"  Atributos: {vars(cuadro)}")
        print()

if __name__ == "__main__":
    main()