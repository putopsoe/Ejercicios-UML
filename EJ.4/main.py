from etapa import EtapaConstruccion
from lugar import Lugar
from edificio import Edificio

def main():
    # Etapas
    ec1 = EtapaConstruccion("Primera etapa", fecha_inicio=1075, fecha_fin=1122)
    ec2 = EtapaConstruccion("Segunda etapa", fecha_inicio=1168, fecha_fin=None)

    # Lugar
    l1 = Lugar(ciudad="Santiago de Compostela", comunidad="Galicia", pais="España", titulo="Centro de La Coruña")

    # Edificio (Catedral)
    catedral = Edificio(
        nombre="Catedral de Santiago de Compostela",
        culto="Católico",
        fecha_inicio_construccion=1075,
        fecha_fin_construccion=1122,
        fecha_primera_consagracion=1128,
        fecha_inicio_segunda_etapa=1168,
        fecha_segunda_consagracion="3 de abril de 1211",
        fecha_declaracion_bic=1896,
        material="Granito",
        estilos=["Románico", "Gótico", "Barroco", "Plateresco", "Neoclásico"]
    )

    # Asociar lugar y etapas
    catedral.set_lugar(l1)
    catedral.add_etapa(ec1)
    catedral.add_etapa(ec2)

    # Mostrar
    print(catedral)
    print()
    print(l1)

if __name__ == "__main__":
    main()