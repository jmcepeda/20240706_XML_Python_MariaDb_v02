import xml.etree.ElementTree as ET
from datetime import datetime

from src.variables_v02 import field_map
# from pymongo import MongoClient

# from pymongo import MongoClient

import sys
# import mariadb

import mysql.connector


# Datos de conexión
try:
    conn = mysql.connector.connect(
        user="jmcepeda",
        password="cintiatyron2015",
        # Para mac
        # host="192.168.50.143",
        # Para Windows/remote
        host="www.multiplicarsantiponce.duckdns.org",
        port=38969,
        database="pruebaxml",
        collation="utf8mb4_unicode_ci"
    )
except mysql.connector.Error as e:
    print(f"Error conectando a la base de datos: {e}")
    sys.exit(1)

SENTENCIASQL = """CREATE TABLE IF NOT EXISTS CEE7
(idCee INT NOT NULL AUTO_INCREMENT,
DateCee DATETIME NOT NULL, 
ReferenciaCatastral VARCHAR(40),
Provincia VARCHAR(40) NOT NULL,
ComunidadAutonoma VARCHAR(40) NOT NULL,
ZonaClimatica VARCHAR(40) NOT NULL,
TipoDeEdificio VARCHAR(40) NOT NULL,
NormativaVigente VARCHAR(40) NOT NULL,
Direccion VARCHAR(40) NOT NULL,
NombreDelEdificio VARCHAR(250) NOT NULL,
SuperficieHabitable DEC(10,6) NOT NULL,
Procedimiento VARCHAR(40) NOT NULL,
AlcanceInformacionXML VARCHAR(40) NOT NULL,
Municipio VARCHAR(40) NOT NULL,
YearConstruccion INT NOT NULL,
PorcentajeSuperficieHabitableCalefactada DEC(18,8) NOT NULL,
DensidadFuentesInternas DEC(18,8) NOT NULL,
Compacidad DEC(18,8) NOT NULL,
VolumenEspacioHabitable DEC(18,8) NOT NULL,
VentilacionTotal DEC(18,8) NOT NULL,
DemandaDiariaACS DEC(18,8) NOT NULL,
NumeroDePlantasSobreRasante DEC(18,8) NOT NULL,
NumeroDePlantasBajoRasante DEC(18,8) NOT NULL,
PorcentajeSuperficieHabitableRefrigerada DEC(18,8) NOT NULL,
PorcentajeSuperficieAcristaladaE DEC(18,8) NOT NULL,
PorcentajeSuperficieAcristaladaNO DEC(18,8) NOT NULL,
PorcentajeSuperficieAcristaladaNE DEC(18,8) NOT NULL,
PorcentajeSuperficieAcristaladaO DEC(18,8) NOT NULL,
PorcentajeSuperficieAcristaladaN DEC(18,8) NOT NULL,
PorcentajeSuperficieAcristaladaS DEC(18,8) NOT NULL,
PorcentajeSuperficieAcristaladaSO DEC(18,8) NOT NULL,
PorcentajeSuperficieAcristaladaSE DEC(18,8) NOT NULL,
DemandaEdificioObjetoGlobal DEC(18,8) NOT NULL,
DemandaEdificioObjetoACS DEC(18,8) NOT NULL,
DemandaEdificioObjetoRefrigeracion DEC(18,8) NOT NULL,
DemandaEdificioObjetoCalefaccion DEC(18,8) NOT NULL,
DemandaEdificioDeReferenciaACS DEC(18,8) NOT NULL,
DemandaEdificioDeReferenciaRefrigeracion DEC(18,8) NOT NULL,
DemandaEdificioDeReferenciaCalefaccion DEC(18,8) NOT NULL,
DemandaEdificioDeReferenciaGlobal DEC(18,8) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableGasNatural DEC(18,8) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableBiomasaOtros DEC(18,8) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableGasoleoC DEC(18,8) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableElectricidadPeninsular DEC(18,8) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableGLP DEC(18,8) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableCarbon DEC(18,8) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableBiocarburante DEC(18,8) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableBiomasaPellet DEC(18,8) NOT NULL,
FactoresdePasoFinalAEmisionesGasNatural DEC(18,8) NOT NULL,
FactoresdePasoFinalAEmisionesBiomasaOtros DEC(18,8) NOT NULL,
FactoresdePasoFinalAEmisionesGasoleoC DEC(18,8) NOT NULL,
FactoresdePasoFinalAEmisionesElectricidadPeninsular DEC(18,8) NOT NULL,
FactoresdePasoFinalAEmisionesGLP DEC(18,8) NOT NULL,
FactoresdePasoFinalAEmisionesCarbon DEC(18,8) NOT NULL,
FactoresdePasoFinalAEmisionesBiocarburante DEC(18,8) NOT NULL,
FactoresdePasoFinalAEmisionesBiomasaPellet DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresGasNaturalCalefaccion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresGasNaturalGlobal DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresGasNaturalACS DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresGasNaturalRefrigeracion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresGasNaturalIluminacion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresElectricidadPeninsularCalefaccion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresElectricidadPeninsularGlobal DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresElectricidadPeninsularACS DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresElectricidadPeninsularRefrigeracion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresElectricidadPeninsularIluminacion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaOtrosCalefaccion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaOtrosGlobal DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaOtrosACS DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaOtrosRefrigeracion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaOtrosIluminacion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresGasoleoCCalefaccion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresGasoleoCGlobal DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresGasoleoCACS DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresGasoleoCRefrigeracion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresGasoleoCIluminacion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresGLPCalefaccion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresGLPGlobal DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresGLPACS DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresGLPRefrigeracion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresGLPIluminacion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresCarbonCalefaccion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresCarbonGlobal DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresCarbonACS DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresCarbonRefrigeracion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresCarbonIluminacion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresBiocarburanteCalefaccion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresBiocarburanteGlobal DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresBiocarburanteACS DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresBiocarburanteRefrigeracion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresBiocarburanteIluminacion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaPelletsCalefaccion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaPelletsGlobal DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaPelletsACS DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaPelletsRefrigeracion DEC(18,8) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaPelletsIluminacion DEC(18,8) NOT NULL,
ConsumoEnergiaPrimariaNoRenovableCalefaccion DEC(18,8) NOT NULL,
ConsumoEnergiaPrimariaNoRenovableGlobal DEC(18,8) NOT NULL,
ConsumoEnergiaPrimariaNoRenovableACS DEC(18,8) NOT NULL,
ConsumoEnergiaPrimariaNoRenovableRefrigeracion DEC(18,8) NOT NULL,
ConsumoEnergiaPrimariaNoRenovableIluminacion DEC(18,8) NOT NULL,
EmisionesCO2ConsumoElectrico DEC(18,8) NOT NULL,
EmisionesCO2TotalConsumoElectrico DEC(18,8) NOT NULL,
EmisionesCO2TotalConsumoOtros DEC(18,8) NOT NULL,
EmisionesCO2Global DEC(18,8) NOT NULL,
EmisionesCO2Calefaccion DEC(18,8) NOT NULL,
EmisionesCO2ACS DEC(18,8) NOT NULL,
EmisionesCO2Refrigeracion DEC(18,8) NOT NULL,
EmisionesCO2Iluminacion DEC(18,8) NOT NULL,
CalificacionDemandaCalefaccion VARCHAR(40) NOT NULL,
CalificacionDemandaRefrigeracion VARCHAR(40) NOT NULL,
CalificacionDemandaEscalaCalefaccionA DEC(18,8) NOT NULL,
CalificacionDemandaEscalaCalefaccionB DEC(18,8) NOT NULL,
CalificacionDemandaEscalaCalefaccionC DEC(18,8) NOT NULL,
CalificacionDemandaEscalaCalefaccionD DEC(18,8) NOT NULL,
CalificacionDemandaEscalaCalefaccionE DEC(18,8) NOT NULL,
CalificacionDemandaEscalaCalefaccionF DEC(18,8) NOT NULL,
CalificacionDemandaEscalaRefrigeracionA DEC(18,8) NOT NULL,
CalificacionDemandaEscalaRefrigeracionB DEC(18,8) NOT NULL,
CalificacionDemandaEscalaRefrigeracionC DEC(18,8) NOT NULL,
CalificacionDemandaEscalaRefrigeracionD DEC(18,8) NOT NULL,
CalificacionDemandaEscalaRefrigeracionE DEC(18,8) NOT NULL,
CalificacionDemandaEscalaRefrigeracionF DEC(18,8) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableCalefaccion VARCHAR(40) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableRefrigeracion VARCHAR(40) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableIluminacion VARCHAR(40) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableGlobal VARCHAR(40) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalA DEC(18,8) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalB DEC(18,8) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalC DEC(18,8) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalD DEC(18,8) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalE DEC(18,8) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalF DEC(18,8) NOT NULL,
CalificacionEmisionesC02Calefaccion VARCHAR(40) NOT NULL,
CalificacionEmisionesC02Refrigeracion VARCHAR(40) NOT NULL,
CalificacionEmisionesC02Iluminacion VARCHAR(40) NOT NULL,
CalificacionEmisionesC02Global VARCHAR(40) NOT NULL,
CalificacionEmisionesC02EscalaGlobalA DEC(18,8) NOT NULL,
CalificacionEmisionesC02EscalaGlobalB DEC(18,8) NOT NULL,
CalificacionEmisionesC02EscalaGlobalC DEC(18,8) NOT NULL,
CalificacionEmisionesC02EscalaGlobalD DEC(18,8) NOT NULL,
CalificacionEmisionesC02EscalaGlobalE DEC(18,8) NOT NULL,
CalificacionEmisionesC02EscalaGlobalF DEC(18,8) NOT NULL,
PRIMARY KEY (idCee) 
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""
cur = conn.cursor()
cur.execute(SENTENCIASQL)
conn.commit()
# conn.close()


# Crear el archivo XML

# Carga y parsea el archivo XML

RUTARCHIVO = "./01_XML_CEE/00_CE3X_GT/20210513_Gran_Terciario_Ejemplo_Sevilla.xml"
RUTARCHIVO = "./01_XML_CEE/00_CE3X_PYMT/3 Pequeno terciario.xml"

tree = ET.parse(RUTARCHIVO)
root = tree.getroot()


def print_element_paths(element, current_path=""):
    # Construye la ruta del elemento actual
    path = f"{current_path}/{element.tag}"

    # Imprime la ruta del elemento actual y su texto si existe
    if element.text and element.text.strip():
        print(f"Path: {path}, Tag: {element.tag}, Text: {element.text.strip()}")
    else:
        print(f"Path: {path}, Text: None")

    # Recorre los hijos del elemento actual
    for child in element:
        print_element_paths(child, path)


# Inicia la función recursiva desde el elemento raíz
print_element_paths(root)

for child in root:
    if child.text and child.text.strip():
        print(f" Tag: {child.tag}, Text: {child.text.strip()}")
    else:
        print(f" Tag: {child.tag}, Text: None")


# Vamos a tratar de identificar un valor en concreto

CalifiacionEmisiones = root.find(
    './/Calificacion/EmisionesCO2/Global')
print(CalifiacionEmisiones.text)


# Especifica los campos a extraer y sus nombres mapeados en la base de datos
# field_map = {
#     # 'ZonaClimatica': 'ZonaClimatica',
#     './/Calificacion/EmisionesCO2/Global': 'CalificacionEmisionesC02Global'
# }

print("Primera Parte de Consulta para Insertar")
print({', '.join(field_map.values())})

print("Segunda Parte de Consulta para Insertar")
print({', '.join(['%s'] * len(field_map))})


print("Imprimir Consulta Completa para Insertar")
print(
    f"INSERT INTO CEE7 ({', '.join(field_map.values())}) VALUES ({', '.join(['%s'] * len(field_map))})")

# Función para detectar y convertir tipos de datos


def convert_type(value):
    # Detectar y convertir enteros
    if value.isdigit():
        return int(value)

    # Detectar y convertir flotantes
    try:
        float_value = float(value)
        return float_value
    except ValueError:
        pass

    # Detectar y convertir fechas
    # Puedes agregar otros formatos de fecha según sea necesario
    date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"]
    for fmt in date_formats:
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            pass

    # Si no es ninguno de los anteriores, retornar como string (cadena de caracteres)
    return value


# Prepara la consulta de inserción con los nombres de las columnas mapeadas
query = f"INSERT INTO CEE7 ({', '.join(field_map.values())}) VALUES({', '.join(['%s'] * len(field_map))})"

# Recorre los elementos del XML y extrae los datos deseados

values = []
for xml_field, db_field in field_map.items():
    # value = root.find(xml_field).text
    print('Campo Analizador para Convertir: ', xml_field)
    # value = convert_type(root.find(xml_field))
    if root.find(xml_field) is not None:
        value = convert_type(root.find(xml_field).text)
    else:
        value = root.find(xml_field).text
    # if xml_field =="DateCee"
    #     value = root.find(xml_field).text

    values.append(value)
    print(xml_field, ' - ', root.find(xml_field).text)

print("Imprimiendo Valores de los campos")
print(tuple(values))

# Inserta los datos en la base de datos
cur.execute(query, tuple(values))

# cur.execute(SENTENCIASQL)

print(values)


# Confirma los cambios
conn.commit()

# Cierra la conexión
cur.close()
conn.close()
