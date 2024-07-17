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
        host="192.168.50.143",
        # Para Windows/remote
        # host="www.multiplicarsantiponce.duckdns.org",
        port=38969,
        database="pruebaxml",
        collation="utf8mb4_unicode_ci"
    )
except mysql.connector.Error as e:
    print(f"Error conectando a la base de datos: {e}")
    sys.exit(1)

SENTENCIASQL = """CREATE TABLE IF NOT EXISTS CEE
(idCee INT NOT NULL AUTO_INCREMENT,
DateRegistro DATETIME NOT NULL,
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
Procedimiento VARCHAR(80) NOT NULL,
AlcanceInformacionXML VARCHAR(40) NOT NULL,
Municipio VARCHAR(40) NOT NULL,
YearConstruccion VARCHAR(40) NOT NULL,
PorcentajeSuperficieHabitableCalefactada DEC(18,8) NOT NULL,
DensidadFuentesInternas DEC(18,8) NOT NULL,
Compacidad DEC(18,8) NOT NULL,
VolumenEspacioHabitable DEC(18,8) NOT NULL,
VentilacionTotal DEC(18,8) NOT NULL,
DemandaDiariaACS DEC(18,8) NOT NULL,
NumeroDePlantasSobreRasante DEC(18,8) NOT NULL,
NumeroDePlantasBajoRasante DEC(18,8) NOT NULL,
PorcentajeSuperficieHabitableRefrigerada DEC(18,8) NOT NULL,
PorcentajeSuperficieAcristaladaE DEC(18,8),
PorcentajeSuperficieAcristaladaNO DEC(18,8),
PorcentajeSuperficieAcristaladaNE DEC(18,8),
PorcentajeSuperficieAcristaladaO DEC(18,8),
PorcentajeSuperficieAcristaladaN DEC(18,8),
PorcentajeSuperficieAcristaladaS DEC(18,8),
PorcentajeSuperficieAcristaladaSO DEC(18,8),
PorcentajeSuperficieAcristaladaSE DEC(18,8),
DemandaEdificioObjetoGlobal DEC(18,8) NOT NULL,
DemandaEdificioObjetoACS DEC(18,8) NOT NULL,
DemandaEdificioObjetoRefrigeracion DEC(18,8) NOT NULL,
DemandaEdificioObjetoCalefaccion DEC(18,8) NOT NULL,
DemandaEdificioDeReferenciaACS DEC(18,8),
DemandaEdificioDeReferenciaRefrigeracion DEC(18,8),
DemandaEdificioDeReferenciaCalefaccion DEC(18,8),
DemandaEdificioDeReferenciaGlobal DEC(18,8),
FactoresdePasoFinalAPrimariaNoRenovableGasNatural DEC(18,8) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableBiomasaOtros DEC(18,8) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableGasoleoC DEC(18,8) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableElectricidadPeninsular DEC(18,8) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableGLP DEC(18,8) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableCarbon DEC(18,8) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableBiocarburante DEC(18,8),
FactoresdePasoFinalAPrimariaNoRenovableBiomasaPellet DEC(18,8) NOT NULL,
FactoresdePasoFinalAEmisionesGasNatural DEC(18,8) NOT NULL,
FactoresdePasoFinalAEmisionesBiomasaOtros DEC(18,8) NOT NULL,
FactoresdePasoFinalAEmisionesGasoleoC DEC(18,8) NOT NULL,
FactoresdePasoFinalAEmisionesElectricidadPeninsular DEC(18,8) NOT NULL,
FactoresdePasoFinalAEmisionesGLP DEC(18,8) NOT NULL,
FactoresdePasoFinalAEmisionesCarbon DEC(18,8) NOT NULL,
FactoresdePasoFinalAEmisionesBiocarburante DEC(18,8),
FactoresdePasoFinalAEmisionesBiomasaPellet DEC(18,8),
ConsumoEnergiaFinalVectoresGasNaturalCalefaccion DEC(18,8),
ConsumoEnergiaFinalVectoresGasNaturalGlobal DEC(18,8),
ConsumoEnergiaFinalVectoresGasNaturalACS DEC(18,8),
ConsumoEnergiaFinalVectoresGasNaturalRefrigeracion DEC(18,8),
ConsumoEnergiaFinalVectoresGasNaturalIluminacion DEC(18,8),
ConsumoEnergiaFinalVectoresElectricidadPeninsularCalefaccion DEC(18,8),
ConsumoEnergiaFinalVectoresElectricidadPeninsularGlobal DEC(18,8),
ConsumoEnergiaFinalVectoresElectricidadPeninsularACS DEC(18,8),
ConsumoEnergiaFinalVectoresElectricidadPeninsularRefrigeracion DEC(18,8),
ConsumoEnergiaFinalVectoresElectricidadPeninsularIluminacion DEC(18,8),
ConsumoEnergiaFinalVectoresBiomasaOtrosCalefaccion DEC(18,8),
ConsumoEnergiaFinalVectoresBiomasaOtrosGlobal DEC(18,8),
ConsumoEnergiaFinalVectoresBiomasaOtrosACS DEC(18,8),
ConsumoEnergiaFinalVectoresBiomasaOtrosRefrigeracion DEC(18,8),
ConsumoEnergiaFinalVectoresBiomasaOtrosIluminacion DEC(18,8),
ConsumoEnergiaFinalVectoresGasoleoCCalefaccion DEC(18,8),
ConsumoEnergiaFinalVectoresGasoleoCGlobal DEC(18,8),
ConsumoEnergiaFinalVectoresGasoleoCACS DEC(18,8),
ConsumoEnergiaFinalVectoresGasoleoCRefrigeracion DEC(18,8),
ConsumoEnergiaFinalVectoresGasoleoCIluminacion DEC(18,8),
ConsumoEnergiaFinalVectoresGLPCalefaccion DEC(18,8),
ConsumoEnergiaFinalVectoresGLPGlobal DEC(18,8),
ConsumoEnergiaFinalVectoresGLPACS DEC(18,8),
ConsumoEnergiaFinalVectoresGLPRefrigeracion DEC(18,8),
ConsumoEnergiaFinalVectoresGLPIluminacion DEC(18,8),
ConsumoEnergiaFinalVectoresCarbonCalefaccion DEC(18,8),
ConsumoEnergiaFinalVectoresCarbonGlobal DEC(18,8),
ConsumoEnergiaFinalVectoresCarbonACS DEC(18,8),
ConsumoEnergiaFinalVectoresCarbonRefrigeracion DEC(18,8),
ConsumoEnergiaFinalVectoresCarbonIluminacion DEC(18,8),
ConsumoEnergiaFinalVectoresBiocarburanteCalefaccion DEC(18,8),
ConsumoEnergiaFinalVectoresBiocarburanteGlobal DEC(18,8),
ConsumoEnergiaFinalVectoresBiocarburanteACS DEC(18,8),
ConsumoEnergiaFinalVectoresBiocarburanteRefrigeracion DEC(18,8),
ConsumoEnergiaFinalVectoresBiocarburanteIluminacion DEC(18,8),
ConsumoEnergiaFinalVectoresBiomasaPelletsCalefaccion DEC(18,8),
ConsumoEnergiaFinalVectoresBiomasaPelletsGlobal DEC(18,8),
ConsumoEnergiaFinalVectoresBiomasaPelletsACS DEC(18,8),
ConsumoEnergiaFinalVectoresBiomasaPelletsRefrigeracion DEC(18,8),
ConsumoEnergiaFinalVectoresBiomasaPelletsIluminacion DEC(18,8),
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
CalificacionDemandaCalefaccion VARCHAR(40),
CalificacionDemandaRefrigeracion VARCHAR(40),
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
CalificacionEnergiaPrimariaNoRenovableCalefaccion VARCHAR(40),
CalificacionEnergiaPrimariaNoRenovableRefrigeracion VARCHAR(40),
CalificacionEnergiaPrimariaNoRenovableIluminacion VARCHAR(40),
CalificacionEnergiaPrimariaNoRenovableGlobal VARCHAR(40),
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalA DEC(18,8) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalB DEC(18,8) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalC DEC(18,8) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalD DEC(18,8) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalE DEC(18,8) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalF DEC(18,8) NOT NULL,
CalificacionEmisionesC02Calefaccion VARCHAR(40),
CalificacionEmisionesC02Refrigeracion VARCHAR(40),
CalificacionEmisionesC02Iluminacion VARCHAR(40),
CalificacionEmisionesC02Global VARCHAR(40),
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
# RUTARCHIVO = "./01_XML_CEE/00_CE3X_PYMT/3_Pequeno_terciario.xml"
# RUTARCHIVO = "./01_XML_CEE/02_HULC/ejemplogt-Certificado-V21.xml"
# RUTARCHIVO = "./01_XML_CEE/01_CYPETHERM/2126PT_Certificacionenergetica_v0_210901_JAGG.xml"


tree = ET.parse(RUTARCHIVO)
root = tree.getroot()


def print_element_paths(element, current_path=""):
    # Construye la ruta del elemento actual
    path = f"{current_path}/{element.tag}"

    # Imprime la ruta del elemento actual y su texto si existe
    if element.text and element.text.strip():
        print(f"Path: {path}, Tag: {element.tag}, Text: {
              element.text.strip()}")
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

# print("Primera Parte de Consulta para Insertar")
# print({', '.join(field_map.values())})

# print("Segunda Parte de Consulta para Insertar")
# print({', '.join(['%s'] * len(field_map))})


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

# Insertar Campos Adicionales en Tupla field_map


my_field_map = {
    'Sin_Datos_en_XML': 'DateRegistro',
}


# Crear un nuevo diccionario con el nuevo elemento al principio

my_field_map.update(field_map)

# Prepara la consulta de inserción con los nombres de las columnas mapeadas
query = f"INSERT INTO CEE ({', '.join(my_field_map.values())}) VALUES({
    ', '.join(['%s'] * len(my_field_map))})"

print("Imprimir Consulta Completa para Insertar")
print(query)

# Recorre los elementos del XML y extrae los datos deseados

values = []
for xml_field, db_field in field_map.items():
    # value = root.find(xml_field).text
    # print('Campo Analizador para Convertir: ', xml_field)
    # value = convert_type(root.find(xml_field))
    if root.find(xml_field) is not None:
        value = convert_type(root.find(xml_field).text)
    else:
        # value = root.find(xml_field).text
        value = None
    # if xml_field =="DateCee"
    #     value = root.find(xml_field).text

    values.append(value)
    print(xml_field, ' - ', value)

# print("Imprimiendo Valores de los campos")
# print(tuple(values))

# Convertir la tupla en una lista

# Nuevo elemento que deseas insertar

# Obtener la fecha y hora actual
fecha_actual = datetime.now()

print(fecha_actual)

# fecha_actual = fecha_actual.strptime(fecha_actual, "%Y-%m-%d")

# Puedes usar lista.insert(posicion, nuevo_elemento) para una posición específica
values.insert(0, fecha_actual)

print("Imprimiendo Valores de los campos Tras Añadir Fecha de Registro")
print(tuple(values))

# Inserta los datos en la base de datos
cur.execute(query, tuple(values))

# cur.execute(SENTENCIASQL)

print(values)


# Confirma los cambios
conn.commit()


# Ahora toca hacer una consulta de datos

# Crear un cursor
cursor = conn.cursor(dictionary=True)

# Consulta para obtener los registros de la tabla de viviendas
consulta_CEE = """
SELECT
    NombreDelEdificio,
    Provincia,
    Municipio,
    ZonaClimatica,
    SuperficieHabitable,
    ReferenciaCatastral,
    Procedimiento,
    YearConstruccion,
    EmisionesCO2Global,
    EmisionesCO2Calefaccion,
    EmisionesCO2ACS,
    EmisionesCO2Refrigeracion,
    EmisionesCO2Iluminacion,
    CalificacionDemandaCalefaccion,
    CalificacionDemandaRefrigeracion,
    CalificacionEmisionesC02Calefaccion,
    CalificacionEmisionesC02Refrigeracion,
    CalificacionEmisionesC02Iluminacion,
    CalificacionEmisionesC02Global,
    ConsumoEnergiaPrimariaNoRenovableCalefaccion,
    ConsumoEnergiaPrimariaNoRenovableGlobal,
    ConsumoEnergiaPrimariaNoRenovableACS,
    ConsumoEnergiaPrimariaNoRenovableRefrigeracion,
    ConsumoEnergiaPrimariaNoRenovableIluminacion,
    CalificacionEnergiaPrimariaNoRenovableCalefaccion,
    CalificacionEnergiaPrimariaNoRenovableRefrigeracion,
    CalificacionEnergiaPrimariaNoRenovableIluminacion,
    CalificacionEnergiaPrimariaNoRenovableGlobal
FROM
    CEE
"""

# Ejecutar la consulta
cursor.execute(consulta_CEE)

# Obtener todos los resultados y almacenarlos en una lista de diccionarios
resultados_CEE = cursor.fetchall()

print(resultados_CEE)

# Cierra la conexión
cur.close()
conn.close()
