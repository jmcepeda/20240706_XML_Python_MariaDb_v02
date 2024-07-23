import xml.etree.ElementTree as ET
from datetime import datetime

from src.variables_v02 import field_map, field_map_cerramiento, field_map_hueco, field_list_equipo
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
IluminacionPotenciaTotalInstalada DEC(18,8),
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
RUTARCHIVO = "./01_XML_CEE/00_CE3X_PYMT/3_Pequeno_terciario.xml"
RUTARCHIVO = "./01_XML_CEE/02_HULC/ejemplogt-Certificado-V21.xml"
RUTARCHIVO = "./01_XML_CEE/01_CYPETHERM/2126PT_Certificacionenergetica_v0_210901_JAGG.xml"


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
        print(f"Path: {path}, Tag: {element.tag}, Text: None")

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

    try:
        if value is None:
            return None
    except ValueError:
        pass

    # Detectar y convertir enteros
    print('value: ', value)
    try:
        if value.isdigit():
            return int(value)
    except ValueError:
        pass

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
query = f"INSERT INTO CEE({', '.join(my_field_map.values())}) VALUES({
    ', '.join(['%s'] * len(my_field_map))})"

print("Imprimir Consulta Completa para Insertar")
# print(query)

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
    # print(xml_field, ' - ', value)

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
# print(tuple(values))

# Inserta los datos en la base de datos
cur.execute(query, tuple(values))

# cur.execute(SENTENCIASQL)

# print(values)


# Confirma los cambios
conn.commit()


idCEE = cur.lastrowid
print("Este es el Id delÚltimo CEE Registrado en la Base de Datos: ", idCEE)

# Ahora Vamos a cargar Cerramientos de un CEE


# Ahora Vamos a Cargar Huecos de un CEE


# Ahora Vamos a Cargar los Equipos de  un ConnectionError
# Para los Equipos Será necesario Generar el fiel_map en Tiempo Real, Adaptado a cada Fichero


for campo in field_list_equipo:
    print(campo[0] + "-" + campo[1])

clase_equipos = []

field_map_equipos = [[]]


def create_field_map_equipos(element, clase_equipos_a, field_list_equipo_a, current_path=""):
    # Construye la ruta del elemento actual
    path = f"{current_path}/{element.tag}"
    # print("Se confirma que entra en la función reate_field_map_equipos")
    # Imprime la ruta del elemento actual y su texto si existe
    count = 0
    # Recorre los hijos del elemento actual
    countClase = 0
    for hijo in element:
        countClase += 1

    for hijo in element:
        # print("Debería entrar cuando esto fuera igual a: InstalacionesTermicas - ", element.tag)
        if element.tag == "InstalacionesTermicas":
            # print("Confirmar que el programa entra en este parte del programa")
            # print("Impriemiendo field_map_equipos_a", field_map_equipos_a)
            clase_equipos_a.append(hijo.tag)

        create_field_map_equipos(
            hijo, clase_equipos_a, field_list_equipo_a,  path)

    return clase_equipos_a


# Voy a rescatar información del ID del Elemento


# Inicia la función recursiva desde el elemento raíz para sacar los tipos de equipos
clase_equipos = create_field_map_equipos(
    root, clase_equipos, field_list_equipo, "")

print("Imprimiendo el mapa de variables de los equipos de Climatización/ACS")
print(field_map_equipos)

print('Imprimiendo Las Clases de Equipos de Climatización y ACS')
print(clase_equipos)

# Ahora Vamos a hacer la consulta para cargar los EQUIPOS de Climatización de un CEE
# Es muy importante ver con chatGPT como identifico el idCee al cual voy a vincular los equipos, huecos, etc

SENTENCIASQL = """CREATE TABLE IF NOT EXISTS EQUIPOSCEE
(idEquipo INT NOT NULL AUTO_INCREMENT,
idCee INT NOT NULL,
climacsDateRegistro DATETIME NOT NULL,
climacsNombre VARCHAR(80) NOT NULL,
climacsClase VARCHAR(80) NOT NULL,
climacsTipo VARCHAR(80) NOT NULL,
climacsPotenciaNominal DEC(14,6),
climacsRendimientoNominal DEC(14,6),
climacsRendimientoEstacional DEC(14,6),
climacsVectorEnergetico VARCHAR(80),
climacsModoDeObtencion VARCHAR(80),
climacsRecuperacionEnergia VARCHAR(80),
climacsServicioAsociado VARCHAR(80),
climacsConsumoDeEnergia DEC(14,6),
climacsEnfriamientoEvaporativo VARCHAR(80),
climacsEnfriamientoGratuito VARCHAR(80),
climacsPotenciaCalor DEC(14,6),
climacsPotenciaFrio DEC(14,6),
climacsRendimientoCalor DEC(14,6),
climacsRendimientoEstacionalCalor DEC(14,6),
climacsRendimientoEstacionalFrio DEC(14,6),
climacsRendimientoFrio DEC(14,6),
climacsZonaAsociada VARCHAR(300),
climacsTipoControl VARCHAR(80),
PRIMARY KEY (idEquipo)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""

# cur = conn.cursor()
cur.execute(SENTENCIASQL)
conn.commit()


def mount_field_map_equipos_all(element, clase_equipos_b, field_map_equipos_b, idCEE_a, current_path=""):
    k = 0
    query_equipos = ""
    for hijo in element:
        j = 0
        idclase = 0
        if element.tag == "InstalacionesTermicas":
            for clase in clase_equipos_b:
                print("clase Equipo: ", clase, " - clase: ", hijo.tag)
                print("clase Equipo: ", str(clase),
                      " - clase: ", str(hijo.tag))
                print("Se Cumple la Condición: ", str(clase) == str(hijo.tag))
                if str(clase) == str(hijo.tag):
                    idclase = j
                j += 1

            for grandchild in hijo:
                r = 0
                my_field_map_equiposs = {
                    # 'Sin_Datos_en_XML0': 'climacsClase',
                    'Sin_Datos_en_XML1': 'idCee',
                    'Sin_Datos_en_XML2': 'DateRegistro'}
                print("my_field_map_equipo : ", my_field_map_equiposs)
                strcampos = "climacsClase, idCee, climacsDateRegistro"
                values_list = []
                print("grandchild.tag: ", grandchild.tag)
                print("idclase: ", idclase)
                print("k: ", k)

                num_campos_equipo = 0
                for campo_c in grandchild:

                    print("campo_c: ", campo_c.tag)
                    strcampos = strcampos + ", climacs" + campo_c.tag
                    #     my_field_map_equiposs
                    value_equipos = convert_type(campo_c.text)
                    values_list.append(value_equipos)
                    num_campos_equipo += 1
                    r += 1
                fecha_actual_equipo = datetime.now()
                values_list.insert(0, fecha_actual_equipo)
                values_list.insert(0, idCEE_a)
                values_list.insert(0, clase_equipos_b[idclase])

                query_equipos = f"INSERT INTO EQUIPOSCEE({strcampos}) VALUES({
                    ', '.join(['%s'] * (num_campos_equipo+3))})"

                print("query_equipos: ", query_equipos)
                print("values: ", values_list)
                cur.execute(query_equipos, tuple(values_list))
                conn.commit()

                k += 1

        mount_field_map_equipos_all(
            hijo, clase_equipos_b, field_map_equipos_b, idCEE_a,  "")
    return


mount_field_map_equipos_all(
    root, clase_equipos, field_map_equipos, idCEE, "")


# Ahora Vamos a Cargar la Envolvente Térmica
# ________________________________________________________
# ________________________________________________________


# Ahora Vamos a Cargar los Equipos de  un ConnectionError
# Para los Equipos Será necesario Generar el fiel_map en Tiempo Real, Adaptado a cada Fichero


clase_cerram_ciego = []

field_map_cerram_ciego = [[]]

field_list_cerram_ciego = []


def create_field_map_cerram_ciegos(element, clase_cerram_ciego_a, field_list_cerram_ciego_a, current_path=""):
    # Construye la ruta del elemento actual
    path = f"{current_path}/{element.tag}"
    # Imprime la ruta del elemento actual y su texto si existe
    count = 0
    # Recorre los hijos del elemento actual
    countClase = 0
    for hijo in element:
        countClase += 1

    for hijo in element:
        # print("Debería entrar cuando esto fuera igual a: InstalacionesTermicas - ", element.tag)
        if element.tag == "DatosEnvolventeTermica":
            # print("Confirmar que el programa entra en este parte del programa")
            # print("Impriemiendo field_map_equipos_a", field_map_equipos_a)
            clase_cerram_ciego_a.append(hijo.tag)
            # for childchild in hijo:

        create_field_map_cerram_ciegos(
            hijo, clase_cerram_ciego_a, field_list_cerram_ciego_a,  path)

    return clase_cerram_ciego_a


# Voy a rescatar información del ID del Elemento


# Inicia la función recursiva desde el elemento raíz para sacar los tipos de equipos
clase_cerram_ciegos = create_field_map_cerram_ciegos(
    root, clase_cerram_ciego, field_list_cerram_ciego, "")


print('Imprimiendo Las Clases de Cerramientos Ciegos')
print(clase_cerram_ciegos)

# Ahora Vamos a hacer la consulta para cargar los EQUIPOS de Climatización de un CEE
# Es muy importante ver con chatGPT como identifico el idCee al cual voy a vincular los equipos, huecos, etc

SENTENCIASQL = """CREATE TABLE IF NOT EXISTS ENVOLVENTETERMICACEE
(idenvolventeTermica INT NOT NULL AUTO_INCREMENT,
idCee INT NOT NULL,
envolventeTermicaDateRegistro DATETIME NOT NULL,
envolventeTermicaNombre VARCHAR(150),
envolventeTermicaClase VARCHAR(80) NOT NULL,
envolventeTermicaTipo VARCHAR(80),
envolventeTermicaCapa VARCHAR(80),
envolventeTermicaTransmitancia DEC(14,6),
envolventeTermicaModoDeObtencionTransmitancia VARCHAR(80),
envolventeTermicaModoDeObtencion VARCHAR(80),
envolventeTermicaSuperficie DEC(14,6),
envolventeTermicaOrientacion VARCHAR(80),
envolventeTermicaLongitud DEC(14,6),
envolventeTermicaFactorSolar DEC(14,6),
envolventeTermicaModoDeObtencionFactorSolar VARCHAR(80),
PRIMARY KEY (idenvolventeTermica)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""

# cur = conn.cursor()
cur.execute(SENTENCIASQL)
conn.commit()


def mount_field_map_envol_termica_all(element, clase_envol_termica_b, idCEE_a, current_path=""):
    k = 0
    query_envol_termica = ""
    for hijo in element:
        j = 0
        idclase = 0
        if element.tag == "DatosEnvolventeTermica":
            for clase in clase_envol_termica_b:
                print("clase Envolvente Térmica: ",
                      clase, " - clase: ", hijo.tag)
                print("clase Envolvente Térmica: ", str(clase),
                      " - clase: ", str(hijo.tag))
                print("Se Cumple la Condición: ", str(clase) == str(hijo.tag))
                if str(clase) == str(hijo.tag):
                    idclase = j
                j += 1

            for grandchild in hijo:
                r = 0

                strcampos = "envolventeTermicaClase, idCee, envolventeTermicaDateRegistro"
                values_list = []
                print("grandchild.tag: ", grandchild.tag)
                print("idclase: ", idclase)
                print("k: ", k)

                num_campos_envol_termica = 0
                for campo_c in grandchild:

                    print("campo_c: ", campo_c.tag)
                    if campo_c.tag != "Capas":
                        strcampos = strcampos + ", envolventeTermica" + campo_c.tag
                        #     my_field_map_equiposs
                        value_envol_termica = convert_type(campo_c.text)
                        values_list.append(value_envol_termica)
                        num_campos_envol_termica += 1
                        r += 1
                fecha_actual_envol_termica = datetime.now()
                values_list.insert(0, fecha_actual_envol_termica)
                values_list.insert(0, idCEE_a)
                values_list.insert(0, clase_envol_termica_b[idclase])

                query_envol_termica = f"INSERT INTO ENVOLVENTETERMICACEE({strcampos}) VALUES({
                    ', '.join(['%s'] * (num_campos_envol_termica+3))})"

                print("query_envolventeTermica: ", query_envol_termica)
                print("values: ", values_list)
                cur.execute(query_envol_termica, tuple(values_list))
                conn.commit()

                k += 1

        # if campo_c.tag != "capas":
        mount_field_map_envol_termica_all(
            hijo, clase_envol_termica_b, idCEE_a,  "")
    return


mount_field_map_envol_termica_all(
    root, clase_cerram_ciego, idCEE, "")


# ________________________________________________________
# ________________________________________________________


# Ahora Vamos a Cargar la Iluminación
# ________________________________________________________
# ________________________________________________________


clase_ciluminación = []

field_map_iluminación = [[]]

field_list_iluminacion = []


SENTENCIASQL = """CREATE TABLE IF NOT EXISTS ILUMINACIONCEE
(idiluminacion INT NOT NULL AUTO_INCREMENT,
idCee INT NOT NULL,
iluminacionDateRegistro DATETIME NOT NULL,
iluminacionNombre VARCHAR(150),
iluminacionModoDeObtencion VARCHAR(80),
iluminacionVEEI DEC(14,6),
iluminacionIluminanciaMedia DEC(14,6),
iluminacionPotenciaInstalada DEC(14,6),
PRIMARY KEY (idiluminacion)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""

# cur = conn.cursor()
cur.execute(SENTENCIASQL)
conn.commit()


def mount_field_map_iluminacion_all(element, idCEE_a, current_path=""):
    k = 0
    query_envol_termica = ""
    for hijo in element:
        j = 0
        # idclase = 0
        if (str(element.tag) == "InstalacionesIluminacion") & (str(hijo.tag) != 'PotenciaTotalInstalada'):

            # for grandchild in hijo:
            r = 0

            strcampos = "idCee, iluminacionDateRegistro"
            values_list = []
            # print("grandchild.tag: ", grandchild.tag)
            # print("idclase: ", idclase)
            print("k: ", k)

            num_campos_iluminacion = 0
            for campo_c in hijo:

                print("campo_c: ", campo_c.tag)
                if campo_c.tag != "Capas":
                    strcampos = strcampos + ", iluminacion" + campo_c.tag
                    #     my_field_map_equiposs
                    value_iluminacion = convert_type(campo_c.text)
                    values_list.append(value_iluminacion)
                    num_campos_iluminacion += 1
                    r += 1
            fecha_actual_iluminacion = datetime.now()
            values_list.insert(0, fecha_actual_iluminacion)
            values_list.insert(0, idCEE_a)
            # values_list.insert(0, clase_iluminacion_b[idclase])

            query_iluminacion = f"INSERT INTO ILUMINACIONCEE ({strcampos}) VALUES({
                ', '.join(['%s'] * (num_campos_iluminacion+2))})"

            print("query_iluminacion: ", query_iluminacion)
            print("values: ", values_list)
            cur.execute(query_iluminacion, tuple(values_list))
            conn.commit()

            k += 1

        # if campo_c.tag != "capas":
        mount_field_map_iluminacion_all(hijo, idCEE_a,  "")
    return


mount_field_map_iluminacion_all(root, idCEE, "")


# ________________________________________________________
# ________________________________________________________


# Ahora Vamos a Cargar las Condiciones de Funcionamiento Zonas
# ________________________________________________________
# ________________________________________________________


clase_zonas = []

field_map_zonas = [[]]

field_list_zonas = []


SENTENCIASQL = """CREATE TABLE IF NOT EXISTS ZONASCEE
(idzona INT NOT NULL AUTO_INCREMENT,
idCee INT NOT NULL,
zonaDateRegistro DATETIME NOT NULL,
zonaNombre VARCHAR(150),
zonaNivelDeAcondicionamiento VARCHAR(80),
zonaPerfilDeUso VARCHAR(80),
zonaSuperficie DEC(14,6),
PRIMARY KEY (idzona)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""

# cur = conn.cursor()
cur.execute(SENTENCIASQL)
conn.commit()


def mount_field_map_zona_all(element, idCEE_a, current_path=""):
    k = 0
    query_envol_termica = ""
    for hijo in element:
        j = 0
        # idclase = 0
        if (str(element.tag) == "CondicionesFuncionamientoyOcupacion"):

            # for grandchild in hijo:
            r = 0

            strcampos = "idCee, zonaDateRegistro"
            values_list = []
            # print("grandchild.tag: ", grandchild.tag)
            # print("idclase: ", idclase)
            print("k: ", k)

            num_campos_zona = 0
            for campo_c in hijo:

                print("campo_c: ", campo_c.tag)
                if campo_c.tag != "Capas":
                    strcampos = strcampos + ", zona" + campo_c.tag
                    #     my_field_map_equiposs
                    value_zona = convert_type(campo_c.text)
                    values_list.append(value_zona)
                    num_campos_zona += 1
                    r += 1
            fecha_actual_zona = datetime.now()
            values_list.insert(0, fecha_actual_zona)
            values_list.insert(0, idCEE_a)
            # values_list.insert(0, clase_iluminacion_b[idclase])

            query_zona = f"INSERT INTO ZONASCEE ({strcampos}) VALUES({
                ', '.join(['%s'] * (num_campos_zona+2))})"

            print("query_iluminacion: ", query_zona)
            print("values: ", values_list)
            cur.execute(query_zona, tuple(values_list))
            conn.commit()

            k += 1

        # if campo_c.tag != "capas":
        mount_field_map_zona_all(hijo, idCEE_a,  "")
    return


mount_field_map_zona_all(root, idCEE, "")


# ________________________________________________________
# ________________________________________________________


# # print_element_paths(root)

# # Ahora toca hacer una consulta de datos

# # Crear un cursor
# cursor = conn.cursor(dictionary=True)

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
cur.execute(consulta_CEE)

# Obtener todos los resultados y almacenarlos en una lista de diccionarios
resultados_CEE = cur.fetchall()

# Imprimir Resultado de la consulta
# print(resultados_CEE)

# Obtener Datos Agregados de tabla CEE

consulta_CEE_Agrupada = """
SELECT
    Provincia,
    COUNT(*) AS Numero_CEE,
    SUM(SuperficieHabitable) AS SuperficieHabitable,
    SUM(EmisionesCO2Global) AS EmisionesCO2Global_Total,
    SUM(EmisionesCO2Global) AS EmisionesCO2Calefaccion_Total,
    SUM(EmisionesCO2Global) AS EmisionesCO2Refrigeración_Total,
    SUM(EmisionesCO2Global) AS EmisionesCO2ACS_Total,
    SUM(EmisionesCO2Global) AS EmisionesCO2Iluminacion_Total,
    SUM(EmisionesCO2Global) AS ConsumoEnergiaPrimariaNoRenovableGlobal_Total,
    SUM(EmisionesCO2Global) AS ConsumoEnergiaPrimariaNoRenovableCalefaccion_Total,
    SUM(EmisionesCO2Global) AS ConsumoEnergiaPrimariaNoRenovableRefrigeración_Total,
    SUM(EmisionesCO2Global) AS ConsumoEnergiaPrimariaNoRenovableACSn_Total,
    SUM(EmisionesCO2Global) AS ConsumoEnergiaPrimariaNoRenovableIluminacion_Total,
    COUNT(DISTINCT Municipio) AS Numero_Municipios
FROM
    CEE
GROUP BY
    Provincia;
"""

# Ejecutar la consulta
cur.execute(consulta_CEE_Agrupada)

# Obtener todos los resultados y almacenarlos en una lista de diccionarios
resultados_CEE_Agrupada = cur.fetchall()

print("                        ")

# Imprimir Resultado de la consulta
Suma_SuperficieHabitable = 0
# print(resultados_CEE)
for registro in resultados_CEE_Agrupada:
    print("  ")
    print(registro)
    # if registro["SuperficieHabitable"] is not None:
    Suma_SuperficieHabitable += float(registro[2])

print(f"SuperficieHabitable Total: {Suma_SuperficieHabitable} m2")
# Hacer Operaciones con datos de la Base de Datos
print(
    f"Tres Veces la Suma de la SuperficieHabitable Total: {float(Suma_SuperficieHabitable)*3} m2")


# Cierra la conexión
cur.close()
conn.close()
