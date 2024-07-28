import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select
from sqlalchemy.orm import sessionmaker
import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

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
        database="prueba_webscraplng",
        collation="utf8mb4_unicode_ci"
    )
except mysql.connector.Error as e:
    print(f"Error conectando a la base de datos: {e}")
    sys.exit(1)


cur = conn.cursor()


SENTENCIASQL = """CREATE TABLE IF NOT EXISTS ESTADO_TARIFA (
    id INT UNSIGNED PRIMARY KEY NOT NULL,
    descripcion VARCHAR(20) NOT NULL
);
"""
cur.execute(SENTENCIASQL)
conn.commit()

SENTENCIASQL = """
INSERT INTO ESTADO_TARIFA (id, descripcion) VALUES
(1, 'Tarifa Actual'),
(2, 'Tarifa Anterior');
"""
cur.execute(SENTENCIASQL)
conn.commit()

SENTENCIASQL = """CREATE TABLE IF NOT EXISTS TIPO_TARIFA (
    id INT UNSIGNED PRIMARY KEY NOT NULL,
    descripcion VARCHAR(60) NOT NULL);
"""
cur.execute(SENTENCIASQL)
conn.commit()

SENTENCIASQL = """
INSERT INTO TIPO_TARIFA (id, descripcion) VALUES
(1, 'Sin Discrimacion Horaria'),
(2, 'Con Discriminación Horaria Tipo 1'),
(3, 'Con Discriminación Horaria Tipo 2'),
(4, 'Indexada PVPC');
"""
cur.execute(SENTENCIASQL)
conn.commit()

SENTENCIASQL = """CREATE TABLE TARIFAS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    comercializadora VARCHAR(80) NOT NULL,
    tarifa VARCHAR(50) NOT NULL,
    ESTADO_ID INT UNSIGNED NOT NULL,
    TIPO_TARIFA_ID INT UNSIGNED NOT NULL,
    precio_potencia_P1 DECIMAL(10, 2) NOT NULL,
    precio_potencia_P2 DECIMAL(10, 2) NOT NULL,
    precio_energia_P1 DECIMAL(10, 2) NOT NULL,
    precio_energia_P2 DECIMAL(10, 2),
    precio_energia_P3 DECIMAL(10, 2),
    estado_id TINYINT UNSIGNED NOT NULL,
    tipo_tarifa_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (ESTADO_ID) REFERENCES ESTADO_TARIFA(id), 
    FOREIGN KEY (TIPO_TARIFA_ID) REFERENCES TIPO_TARIFA(id)
);
"""
cur.execute(SENTENCIASQL)

conn.commit()

cur.close()
conn.close()
