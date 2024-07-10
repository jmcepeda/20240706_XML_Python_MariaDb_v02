import xml.etree.ElementTree as ET
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

SENTENCIASQL = """CREATE TABLE IF NOT EXISTS CEE3
(idCee INT NOT NULL AUTO_INCREMENT,
DatosEnergeticosDelEdificioVersion VARCHAR(40) NOT NULL, 
Descripcioncee VARCHAR(40) NOT NULL,
DatosEnergeticosDelEdificio VARCHAR(40) NOT NULL,
Dateregistro DATETIME NOT NULL,
DateCee DATETIME NOT NULL,
SuperficieHabitable DEC(7,4) NOT NULL,
ReferenciaCatastral VARCHAR(40),
Provincia VARCHAR(40) NOT NULL,
ZonaClimatica VARCHAR(40) NOT NULL,
TipoDeEdificio VARCHAR(40) NOT NULL,
NormativaVigente VARCHAR(40) NOT NULL,
Direccion VARCHAR(40) NOT NULL,
NombreDelEdificio VARCHAR(40) NOT NULL,
Procedimiento VARCHAR(40) NOT NULL,
AlcanceInformacionXML VARCHAR(40) NOT NULL,
Municipio VARCHAR(40) NOT NULL,
YearConstruccion INT NOT NULL,
PorcentajeSuperficieHabitableCalefactada DEC(4,4) NOT NULL,
DensidadFuentesInternas DEC(7,4) NOT NULL,
Compacidad DEC(7,4) NOT NULL,
VolumenEspacioHabitable DEC(7,4) NOT NULL,
VentilacionTotal DEC(7,4) NOT NULL,
DemandaDiariaACS DEC(7,4) NOT NULL,
NumeroDePlantasBajoRasante DEC(4,4) NOT NULL,
PorcentajeSuperficieHabitableRefrigerada DEC(4,4) NOT NULL,
PorcentajeSuperficieAcristaladaE DEC(4,4) NOT NULL,
PorcentajeSuperficieAcristaladaNO DEC(4,4) NOT NULL,
PorcentajeSuperficieAcristaladaNE DEC(4,4) NOT NULL,
PorcentajeSuperficieAcristaladaO DEC(4,4) NOT NULL,
PorcentajeSuperficieAcristaladaN DEC(4,4) NOT NULL,
PorcentajeSuperficieAcristaladaS DEC(4,4) NOT NULL,
PorcentajeSuperficieAcristaladaSO DEC(4,4) NOT NULL,
PorcentajeSuperficieAcristaladaSE DEC(4,4) NOT NULL,
DemandaEdificioObjetoGlobal DEC(7,4) NOT NULL,
DemandaEdificioObjetoACS DEC(7,4) NOT NULL,
DemandaEdificioObjetoRefrigeracion DEC(7,4) NOT NULL,
DemandaEdificioObjetoCalefaccion DEC(7,4) NOT NULL,
DemandaEdificioReferenciaGlobal DEC(7,4) NOT NULL,
DemandaEdificioDeReferenciaACS DEC(7,4) NOT NULL,
DemandaEdificioDeReferenciaRefrigeracion DEC(7,4) NOT NULL,
DemandaEdificioDeReferenciaCalefaccion DEC(7,4) NOT NULL,
DemandaEdificioDeReferenciaGlobal DEC(7,4) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableGasNatural DEC(7,4) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableBiomasaOtros DEC(7,4) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableGasoleoC DEC(7,4) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableElectricidadPeninsular DEC(7,4) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableGLP DEC(7,4) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableCarbon DEC(7,4) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableBiocarburante DEC(7,4) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableElectricidadCanarias DEC(7,4) NOT NULL,
FactoresdePasoFinalAPrimariaNoRenovableBiomasaPellet DEC(7,4) NOT NULL,
FactoresdePasoFinalAEmisionesGasNatural DEC(7,4) NOT NULL,
FactoresdePasoFinalAEmisionesBiomasaOtros DEC(7,4) NOT NULL,
FactoresdePasoFinalAEmisionesGasoleoC DEC(7,4) NOT NULL,
FactoresdePasoFinalAEmisionesElectricidadPeninsular DEC(7,4) NOT NULL,
FactoresdePasoFinalAEmisionesGLP DEC(7,4) NOT NULL,
FactoresdePasoFinalAEmisionesCarbon DEC(7,4) NOT NULL,
FactoresdePasoFinalAEmisionesBiocarburante DEC(7,4) NOT NULL,
FactoresdePasoFinalAEmisionesElectricidadCanarias DEC(7,4) NOT NULL,
FactoresdePasoFinalAEmisionesBiomasaPellet DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresGasNaturalCalefaccion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresGasNaturalGlobal DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresGasNaturalACS DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresGasNaturalRefrigeracion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresGasNaturalIluminacion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresElectricidadPeninsularCalefaccion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresElectricidadPeninsularGlobal DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresElectricidadPeninsularACS DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresElectricidadPeninsularRefrigeracion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresElectricidadPeninsularIluminacion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaOtrosCalefaccion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaOtrosGlobal DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaOtrosACS DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaOtrosRefrigeracion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaOtrosIluminacion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresGasoleoCCalefaccion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresGasoleoCGlobal DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresGasoleoCACS DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresGasoleoCRefrigeracion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresGasoleoCIluminacion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresGLPCalefaccion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresGLPGlobal DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresGLPACS DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresGLPRefrigeracion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresGLPIluminacion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresCarbonCalefaccion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresCarbonGlobal DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresCarbonACS DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresCarbonRefrigeracion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresCarbonIluminacion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresBiocarburantesCalefaccion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresBiocarburantesGlobal DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresBiocarburantesACS DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresBiocarburantesRefrigeracion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresBiocarburantesIluminacion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaPelletsCalefaccion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaPelletsGlobal DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaPelletsACS DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaPelletsRefrigeracion DEC(7,4) NOT NULL,
ConsumoEnergiaFinalVectoresBiomasaPelletsIluminacion DEC(7,4) NOT NULL,
ConsumoEnergiaPrimariaNoRenovableCalefaccion DEC(7,4) NOT NULL,
ConsumoEnergiaPrimariaNoRenovableGlobal DEC(7,4) NOT NULL,
ConsumoEnergiaPrimariaNoRenovableACS DEC(7,4) NOT NULL,
ConsumoEnergiaPrimariaNoRenovableRefrigeracion DEC(7,4) NOT NULL,
ConsumoEnergiaPrimariaNoRenovableIluminacion DEC(7,4) NOT NULL,
EmisionesCO2ConsumoElectrico DEC(7,4) NOT NULL,
EmisionesCO2CTotalConsumoElectrico DEC(7,4) NOT NULL,
EmisionesCO2TotalConsumoOtros DEC(7,4) NOT NULL,
EmisionesCO2Global DEC(7,4) NOT NULL,
EmisionesCO2Calefaccion DEC(7,4) NOT NULL,
EmisionesCO2ACS DEC(7,4) NOT NULL,
EmisionesCO2Refrigeracion DEC(7,4) NOT NULL,
EmisionesCO2Iluminacion DEC(7,4) NOT NULL,
CalificacionDemandaCalefaccion DEC(7,4) NOT NULL,
CalificacionDemandaRefrigeracion DEC(7,4) NOT NULL,
CalificacionDemandaEscalaCalefaccionA DEC(7,4) NOT NULL,
CalificacionDemandaEscalaCalefaccionB DEC(7,4) NOT NULL,
CalificacionDemandaEscalaCalefaccionC DEC(7,4) NOT NULL,
CalificacionDemandaEscalaCalefaccionD DEC(7,4) NOT NULL,
CalificacionDemandaEscalaCalefaccionE DEC(7,4) NOT NULL,
CalificacionDemandaEscalaCalefaccionF DEC(7,4) NOT NULL,
CalificacionDemandaEscalaRefrigeracionA DEC(7,4) NOT NULL,
CalificacionDemandaEscalaRefrigeracionB DEC(7,4) NOT NULL,
CalificacionDemandaEscalaRefrigeracionC DEC(7,4) NOT NULL,
CalificacionDemandaEscalaRefrigeracionD DEC(7,4) NOT NULL,
CalificacionDemandaEscalaRefrigeracionE DEC(7,4) NOT NULL,
CalificacionDemandaEscalaRefrigeracionF DEC(7,4) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableCalefaccion DEC(7,4) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableRefrigeracion DEC(7,4) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableIluminacion DEC(7,4) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableGlobal DEC(7,4) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalA DEC(7,4) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalB DEC(7,4) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalC DEC(7,4) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalD DEC(7,4) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalE DEC(7,4) NOT NULL,
CalificacionEnergiaPrimariaNoRenovableEscalaGlobalF DEC(7,4) NOT NULL,
CalificacionEmisionesC02Calefaccion DEC(7,4) NOT NULL,
CalificacionEmisionesC02Refrigeracion DEC(7,4) NOT NULL,
CalificacionEmisionesC02Iluminacion DEC(7,4) NOT NULL,
CalificacionEmisionesC02Global DEC(7,4) NOT NULL,
CalificacionEmisionesC02EscalaGlobalA DEC(7,4) NOT NULL,
CalificacionEmisionesC02EscalaGlobalB DEC(7,4) NOT NULL,
CalificacionEmisionesC02EscalaGlobalC DEC(7,4) NOT NULL,
CalificacionEmisionesC02EscalaGlobalD DEC(7,4) NOT NULL,
CalificacionEmisionesC02EscalaGlobalE DEC(7,4) NOT NULL,
CalificacionEmisionesC02EscalaGlobalF DEC(7,4) NOT NULL,
PRIMARY KEY (idCee)
);
"""
cur = conn.cursor()
cur.execute(SENTENCIASQL)
conn.commit()
# conn.close()


# Crear el archivo XML

# Carga y parsea el archivo XML

RUTARCHIVO = "./01_XML_CEE/00_CE3X_GT/20210513_Gran_Terciario_Ejemplo_Sevilla.xml"
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
field_map = {
    # 'ZonaClimatica': 'ZonaClimatica',
    './/Calificacion/EmisionesCO2/Global': 'CalificacionEmisionesC02Global'
}

print("Primera Parte de Consulta para Insertar")
print({', '.join(field_map.values())})

print("Segunda Parte de Consulta para Insertar")
print({', '.join(['%s'] * len(field_map))})


print("Imprimir Consulta Completa para Insertar")
print(
    f"INSERT INTO CEE3 ({', '.join(field_map.values())}) VALUES ({', '.join(['%s'] * len(field_map))})")


# Prepara la consulta de inserción con los nombres de las columnas mapeadas
query = f"INSERT INTO CEE3 ({', '.join(field_map.values())}) VALUES ({
    ', '.join(['%s'] * len(field_map))})"

# Recorre los elementos del XML y extrae los datos deseados

values = []
for xml_field, db_field in field_map.items():
    value = root.find(xml_field).text
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
