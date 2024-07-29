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

# """ # Datos de conexión
# try:
#     conn = mysql.connector.connect(
#         user="jmcepeda",
#         password="cintiatyron2015",
#         # Para mac
#         host="192.168.50.143",
#         # Para Windows/remote
#         # host="www.multiplicarsantiponce.duckdns.org",
#         port=38969,
#         database="prueba_webscraplng",
#         collation="utf8mb4_unicode_ci"
#     )
# except mysql.connector.Error as e:
#     print(f"Error conectando a la base de datos: {e}")
#     sys.exit(1)


# cur = conn.cursor()


# SENTENCIASQL = """CREATE TABLE IF NOT EXISTS ESTADO_TARIFA (
#     id INT UNSIGNED PRIMARY KEY NOT NULL,
#     descripcion VARCHAR(20) NOT NULL
# );
# """
# cur.execute(SENTENCIASQL)
# conn.commit()

# estados_tarifas_Table = cur.execute(
#     ("""SELECT COUNT(*) FROM ESTADO_TARIFA"""))
# # Obtener el primer valor de la primera fila
# num_estado_tarifa = cur.fetchall()

# if num_estado_tarifa is None:
#     SENTENCIASQL = """
#     INSERT INTO ESTADO_TARIFA(id, descripcion) VALUES
#     (1, 'Tarifa Actual'),
#     (2, 'Tarifa Anterior');
#     """
#     cur.execute(SENTENCIASQL)
#     conn.commit()

# SENTENCIASQL = """CREATE TABLE IF NOT EXISTS TIPO_TARIFA(
#     id INT UNSIGNED PRIMARY KEY NOT NULL,
#     descripcion VARCHAR(60) NOT NULL);
# """
# cur.execute(SENTENCIASQL)
# conn.commit()


# tipos_tarifas_Table = cur.execute(("""SELECT COUNT(*) FROM TIPO_TARIFA"""))
# # Obtener el primer valor de la primera fila
# num_tipo_tarifa = cur.fetchall()

# if num_tipo_tarifa is None:
#     SENTENCIASQL = """
#     INSERT INTO TIPO_TARIFA(id, descripcion) VALUES
#     (1, 'Sin Discrimacion Horaria'),
#     (2, 'Con Discriminación Horaria Tipo 1'),
#     (3, 'Con Discriminación Horaria Tipo 2'),
#     (4, 'Indexada PVPC');
#     """
#     cur.execute(SENTENCIASQL)
#     conn.commit()

# SENTENCIASQL = """CREATE TABLE IF NOT EXISTS TARIFAS(
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     comercializadora VARCHAR(80) NOT NULL,
#     tarifa VARCHAR(50) NOT NULL,
#     ESTADO_ID INT UNSIGNED NOT NULL,
#     TIPO_TARIFA_ID INT UNSIGNED NOT NULL,
#     precio_potencia_P1 DECIMAL(10, 2) NOT NULL,
#     precio_potencia_P2 DECIMAL(10, 2) NOT NULL,
#     precio_energia_P1 DECIMAL(10, 2) NOT NULL,
#     precio_energia_P2 DECIMAL(10, 2),
#     precio_energia_P3 DECIMAL(10, 2),
#     FOREIGN KEY(ESTADO_ID) REFERENCES ESTADO_TARIFA(id),
#     FOREIGN KEY(TIPO_TARIFA_ID) REFERENCES TIPO_TARIFA(id)
# );
# """
# cur.execute(SENTENCIASQL)

# conn.commit()

# cur.close()
# conn.close() """


# Definir la URL de la comercializadora
# Reemplazar con la URL real
url = 'https://www.naturgy.es/hogar/luz/tarifa_por_uso_luz'


def obtener_precio():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Navegar por los divs anidados
    contenedor = soup.find('div', class_='container')
    if contenedor:
        print("Localizó Contenedor: ")
        row = soup.find('div', class_='row')
        if row:
            print("Localizó row: ")
            faqssection = soup.find('div', class_='faqs-section')
            if faqssection:
                print("Localizó faqssection: ")
                faqscontainer = soup.find('div', class_='faqs-container')
                if faqscontainer:
                    print("Localizó faqscontainer: ")
                    moreinfo = soup.find(
                        'div', class_='moreInfoDetail1-1615661069440')
                    if moreinfo:
                        print("Localizó moreinfo: ")
                        colfaqs = soup.find('div', class_='col-faqs')
                        if colfaqs:
                            print("Localizó colfaqs: ")
                            tabla1id = soup.find('div', id='Tabla1')
                            if tabla1id:
                                print("Localizado tabla1Id: ")
                                containertabla1 = soup.find(
                                    'div', class_='container-tabla-1 tabla1')
                                if containertabla1:
                                    print("Localizó container-tabla-1 tabla1: ")
                                    tabla_potencia = soup.find(
                                        'div', class_='tablaEnergia')
                                    if tabla_potencia:
                                        print("Localizó ctablaEnergia: ")
                                        div_precios = tabla_potencia.find(
                                            'div', class_='divPrecios')
                                        if div_precios:
                                            print("Localizaod divPrecios: ")
                                            textH = div_precios.find(
                                                'div', class_='textH')
                                            if textH:
                                                print("Localizado textH: ")
                                                precio = textH.find(
                                                    'div', class_='precio').text
                                                return precio
    return None


precio = obtener_precio()
precio = precio.replace(',', '.')
preciodef = float(precio[:8])

if precio:
    print(f'El precio de la tarifa es: {preciodef}')
else:
    print('No se encontró el precio de la tarifa.')

# if __name__ == "__main__":
#     precio = obtener_precio()
#     if precio:
#         print(f'El precio de la tarifa es: {precio}')
#     else:
#         print('No se encontró el precio de la tarifa.')


# <div class="tablaPotencia" data-table="p1" data-algo="0" data-typevalor="NO IVA" data-potencia="Potencia ≤10kW" data-assetid="1615692614551"><div class="titulo">Término de potencia</div><div class="container-div-horarios-precios"><div class="divHorarios" >
#                                 <div class="textH">
#                                     <div class="horario">De 08h a 00h (de lunes a viernes) Período Punta (P1)</div>
#                                 </div>
#                                 <div class="textH">
#                                     <div class="horario">De 00h a 08h (de lunes a viernes) y las 24h (fines de semana y festivos) Período Valle (P2)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px;" data-table="p1" data-algo="0" data-typevalor="NO IVA" data-potencia="Potencia ≤10kW" data-assetid="1615692614551"><div class="textH"><div class="precio">0,103663€/kW*día</div></div><!-- 5 --><div class="textH"><div class="precio">0,034042€/kW*día</div></div><!-- 5 --></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --><div class="tablaEnergia" data-table="p1" data-algo="2" data-typevalor="NO IVA" data-potencia="Potencia ≤10kW" data-assetid="1615692614551"><div class="titulo">Término de energía</div><div class="container-div-horarios-precios"><div class="divHorarios" style="height: 120px;">
#                                 <div class="textH">


# <div class="container">
#                 <div class="row">


#                 <!-- Si hemos arrastrado una recomendacion al bloqueLayout... -->


# <div class="faqs-section">


#           <div class="text-center titulo">
#           <p class="h2-restyling ancla" id="precios-y-condiciones">Nuestro precio fijo de luz</p>
#           </div>


#                                           <script>
#                                             $(document).ready(function(){
#                                                     var titlePage = $(document).attr("title");
#                                                     $('.tog-faq1-1615661069440').click(function() {

#                                                         if($('.moreInfoDetail1-1615661069440').css('display') == 'none'){

#                                                             $('.tog-faq1-1615661069440 svg').css({'transform': 'rotate(-180deg)'});

#                                                         }else{

#                                                             $('.tog-faq1-1615661069440 svg').css({'transform': 'rotate(-360deg)'});
#                                                         }

#                                                         $('.moreInfoDetail1-1615661069440').toggle('slow');

#                                                     });
#                                             });
#                                           </script>
#                                                   <div class="faqs-container">


# 																<div class="faqs-fila tog-faq1-1615661069440" onclick="javascript:dataLayer.push({'event':'event.naturgy','eventCategory':'desplegable','eventAction': 'saber mas','eventLabel':'GNF - Tarifa Por Uso Luz - Precios'});">


#                                                                   <div class="texto-faqs">
#                                                                       <p class="moreInfo">Precios</p>
#                                                                   </div>

#                                                                   <div class="img-faqs">
#                                                                             <svg width="16" height="10" viewBox="0 0 16 10" fill="none" xmlns="http://www.w3.org/2000/svg" style="transform : rotate(-180deg)">
#                                                                                 <path d="M7.90362 8.80881C7.90319 8.80856 7.90278 8.80831 7.90238 8.80807L7.8916 8.80175L7.8909 8.80128L7.88576 8.79816C7.87486 8.78748 7.86391 8.77768 7.85319 8.76874C7.84622 8.76209 7.83996 8.75642 7.83474 8.75181C7.83396 8.75112 7.83319 8.75044 7.83242 8.74977L0.559323 0.871814L0.559088 0.871559C0.47633 0.782044 0.481023 0.641484 0.569942 0.557569C0.654991 0.477306 0.785344 0.481 0.866273 0.568536L7.63399 7.89873L8.00144 8.29673L8.3688 7.89865L15.1322 0.569719C15.2144 0.482661 15.3489 0.481614 15.4296 0.557569C15.5199 0.642744 15.522 0.786693 15.4435 0.871703L15.4434 0.871819L8.17344 8.74658C8.17268 8.74725 8.17191 8.74793 8.17112 8.74862C8.16508 8.75397 8.15764 8.76073 8.14933 8.76877C8.1439 8.77333 8.13786 8.77857 8.13137 8.78451C8.12427 8.79057 8.11718 8.79613 8.11101 8.8006L8.10167 8.80584C8.09773 8.80805 8.09272 8.8106 8.08074 8.81613L8.07444 8.8174L8.04375 8.82903L8.03307 8.83175L8.03256 8.83188C8.02672 8.83284 8.02127 8.83372 8.01585 8.83457L8.01572 8.83457L8.00577 8.83459C8.00452 8.83451 8.00266 8.83439 8.0001 8.83421L7.99885 8.83412C7.99399 8.83378 7.98478 8.83314 7.97527 8.83262C7.9648 8.83021 7.95869 8.8286 7.95429 8.8273C7.94635 8.82442 7.93929 8.82201 7.93338 8.82007C7.92742 8.81812 7.92175 8.81634 7.91743 8.81501C7.91109 8.81232 7.90671 8.81031 7.90362 8.80881Z" fill="#004571" stroke="#004571" path="">
#                                                                                     </path>
#                                                                             </svg>
#                                                                         </div>
#                                                             </div>
#                                                             <div class="moreInfoDetail1-1615661069440" style="display: block;">
#                                                                 <div class="col-faqs">


# <script>
#     var iva_1615692614551 = false;
#     var descuento_1615692614551 = false;
#     var potencia_1615692614551 = "Potencia ≤10kW";


#     function updatePrecios_1615692614551(){
#             console.log("updating precionssssss");

#             if(iva_1615692614551&&descuento_1615692614551){
#                 datatypevalor="IVA DESCUENTO";
#             }

#             if(!iva_1615692614551&&descuento_1615692614551){
#                 datatypevalor="NO IVA DESCUENTO";
#             }

#             if(!iva_1615692614551&&!descuento_1615692614551){
#                 datatypevalor="NO IVA";
#             }

#             if(iva_1615692614551&&!descuento_1615692614551){
#                 datatypevalor="IVA";
#             }

#             $("[data-typevalor][data-assetid='1615692614551']").hide();
#             $(".tablaPotencia[data-assetid='1615692614551']").each(function(){
#                 $(this).css('display', 'none');
#             })
#             $(".tablaEnergia[data-assetid='1615692614551']").each(function(){
#                 $(this).css('display', 'none');
#             })
#             //$('div[data-potencia="'+ potencia_1615692614551  +'"][data-typevalor="' + datatypevalor + '"]').css('display', 'grid');
#             $('div[data-potencia="'+ potencia_1615692614551  +'"][data-typevalor="' + datatypevalor + '"][data-assetid="1615692614551"]').css('display', 'grid');
#             $('div.tExcedentes[data-potencia="'+ potencia_1615692614551  +'"][data-typevalor="' + datatypevalor + '"][data-assetid="1615692614551"]').css('display', 'block');

#             /*
#             if (!iva_1615692614551 && !descuento_1615692614551) {
#                 preciot = 'NO IVA';
#             }
#             if (iva_1615692614551 && !descuento_1615692614551) {
#                 preciot = 'IVA';
#             }
#             if (iva_1615692614551 && descuento_1615692614551) {
#                 preciot = 'IVA DESCUENTO';
#             }
#             if (!iva_1615692614551 && descuento_1615692614551) {
#                 preciot = 'NO IVA DESCUENTO';
#             }

#             $('[data-typevalor="'+preciot+'"]').show();
#             */

#         }

#     $(document).ready(function() {
#         $(".selectPotencia2[data-assetid='1615692614551']").click(function() {

#             $(this).find(".options").slideToggle();
#             $(this).toggleClass("active");

#             $(this).find(".options p").click(function(){
#                 console.log($(this).text());
#                 textoPotenciaSelected = $(this).text();
#                 $(this).find(".tablaPotencia[data-assetid='1615692614551']").each(function(){
#                     $(this).css('display', 'none');
#                 });

#                 $(this).find(".tablaEnergia[data-assetid='1615692614551']").each(function(){
#                     $(this).css('display', 'none');
#                 })

#                 //console.log($(this).find(".items > .defaultOption"));

#                 $(".defaultOption[data-assetid='1615692614551']").each(function(){
#                     $(this).text(textoPotenciaSelected);
#                 });

#                 //$(this).find($(".items > .defaultOption").text($(this).text()));
#                 potencia_1615692614551 = $(this).text();

#                 updatePrecios_1615692614551();

#             })
#         });

#         $('.switchIva input[type="checkbox"][data-assetid="1615692614551"]').change(function() {

#             if ($('.switchIva[data-assetid="1615692614551"] span').hasClass('checked')) {
#                 $('.switchIva[data-assetid="1615692614551"] span').removeClass('checked');
#                 $('.switchIva[data-assetid="1615692614551"] .pActive').hide();
#                 $('.switchIva[data-assetid="1615692614551"] .pNoActive').show();
#             } else if (!$('.switchIva[data-assetid="1615692614551"] span').hasClass('checked')) {
#                 $('.switchIva[data-assetid="1615692614551"] .pActive').show();
#                 $('.switchIva[data-assetid="1615692614551"] .pNoActive').hide();
#                 $('.switchIva[data-assetid="1615692614551"] span').addClass('checked');
#             }

#             console.log("switch IVA");
#             iva_1615692614551 = !iva_1615692614551;
#             updatePrecios_1615692614551();
#         });

#         // Capturamos el cambio en el switch de Descuento
#         $('.switchDesc input[type="checkbox"][data-assetid="1615692614551"]').change(function() {

#             if ($('.switchDesc[data-assetid="1615692614551"] span').hasClass('checked')) {
#                 $('.switchDesc[data-assetid="1615692614551"] span').removeClass('checked');
#                 $('.switchDesc[data-assetid="1615692614551"] .pNoActive').show();
#                 $('.switchDesc[data-assetid="1615692614551"] .pActive').hide();
#             } else if (!$('.switchDesc[data-assetid="1615692614551"] span').hasClass('checked')) {
#                 $('.switchDesc[data-assetid="1615692614551"] .pActive').show();
#                 $('.switchDesc[data-assetid="1615692614551"] .pNoActive').hide();
#                 $('.switchDesc[data-assetid="1615692614551"] span').addClass('checked');
#             }

#             console.log("switch Descuentos");
#             descuento_1615692614551 = !descuento_1615692614551;
#             updatePrecios_1615692614551();
#         });


#         updatePrecios_1615692614551(); //actualizamos las tablas en el onready


#         $('#Tabla1.id-1615692614551').show();

#     });


# </script>


#   <style>

# 	#Tabla1 {
# 		display: none;
# 	}

# 	#Tabla1 .container-switches-icons,
# 	#Tabla1 .container-tabla,
# 	#Tabla1 .container-condiciones-impuestos {
# 		margin: 0 auto;
# 		margin-top: 40px;
# 		display: flex;
# 		max-width: 768px;
# 		align-items: flex-end;
# 		justify-content: space-between;
# 		padding: 10px 10px;
# 		height: auto;
# 	}

# 	#Tabla1 .container-condiciones-impuestos {
# 		margin-top: 20px;
# 		display: flex;
# 		flex-direction: column;
# 		align-items: flex-start;
# 		padding: 0 0;
# 		height: auto;
# 	}

# 	#Tabla1 .container-tabla {
# 		padding: 0;
# 		border: solid 1px #004571;
# 		border-radius: 13.27px;
# 		border-top-color: transparent;

# 	}

# 	#Tabla1 .tituloIcon-2 {
# 		gap: 2rem;
# 		display: flex;
# 		align-items: flex-end;
# 		justify-content: flex-start;
# 	}

# 	#Tabla1 .tituloIcon-2 .logo-selectPotencia {
# 		font-weight: 700;
# 	}

# 	#Tabla1 .tituloIcon-2 .logo-selectPotencia span {
# 		font-size: 20px;
# 	}

# 	#Tabla1 .tituloIcon-2 .logo-selectPotencia span.icon {
# 		width: 32px;
# 		height: 32px;
# 		color: #e57200;
# 	}

# 	#Tabla1 .switch-button {
# 		display: flex;
# 		align-items: center;
# 	}

# 	#Tabla1 .switch-button p {
# 		font-size: 16px;
# 		font-weight: 400;
# 		line-height: 12px;
# 		margin-bottom: 0;
# 		color: #767676;
# 		line-height: 17px;

# 	}

# 	#Tabla1 .switch {
# 		position: relative;
# 		width: 60px;
# 		margin: 0;
# 		align-items: center;
# 	}

# 	#Tabla1 .switch input {
# 		opacity: 0;
# 		width: 0;
# 		height: 0;
# 	}

# 	#Tabla1 .switchIva {
# 		margin-bottom: 10px;
# 	}

# 	#Tabla1 .slider-2 {
# 		position: absolute;
# 		cursor: pointer;
# 		top: 0;
# 		left: 0;
# 		right: 0;
# 		bottom: 0;
# 		background-color: #fff;
# 		-webkit-transition: .4s;
# 		transition: .4s;
# 		border: 2px solid #004571;
# 		border-radius: 10px;
# 		width: 42px;
# 		height: 21px;
# 	}

# 	#Tabla1 .slider-2:before {
# 		position: absolute;
# 		content: "";
# 		height: 14px;
# 		width: 14px;
# 		left: 2px;
# 		bottom: 2px;
# 		background-color: #9e9e9e;
# 		-webkit-transition: .4s;
# 		transition: .4s;
# 	}

# 	#Tabla1 input:checked+.slider-2:before {
# 		background-color: #e57200;
# 		/* left: -3px; */
# 	}

# 	#Tabla1 input:checked+.slider-2 {
# 		background-color: #fae2cb;
# 	}

# 	#Tabla1 input:focus+.slider-2 {
# 		box-shadow: 0 0 1px #e57200;
# 	}

# 	#Tabla1 input:checked+.slider-2:before {
# 		-webkit-transform: translateX(21px);
# 		-ms-transform: translateX(21px);
# 		transform: translateX(21px);
# 	}

# 	#Tabla1 .slider-2.round {
# 		border-radius: 34px;
# 	}

# 	#Tabla1 .slider-2.round:before {
# 		border-radius: 50%;
# 	}

# 	#Tabla1 p.pActive {
# 		display: none;
# 	}


# 	#Tabla1 .infoTarifa .title {
# 		color: #e57200;
# 		font-size: 40px;
# 		font-weight: 400;
# 		line-height: 48px;
# 	}

# 	#Tabla1 .tituloIcon-2 p {
# 		color: #004571;
# 		font-size: 32px;
# 		font-weight: 400;
# 		line-height: 39px;
# 		margin-bottom: 0;
# 		margin-left: 15px;
# 	}

# 	#Tabla1 .dropInfo.active svg,
# 	#Tabla1 .dropInfo1.active svg {
# 		transform: rotate(180deg);
# 	}

# 	#Tabla1 .selectPotencia2 {
# 		cursor: pointer;
# 		border-radius: 19.47px;
# 		padding: 9px 12px;
# 		border: 1px solid #004571;
# 		height: fit-content;
# 		display: grid;
# 		width: fit-content;
# 		margin-top: 35px;
# 	}

# 	#Tabla1 .selectPotencia2.active svg {
# 		transform: rotate(180deg);
# 	}

# 	#Tabla1 .selectPotencia2 .items {
# 		display: flex;
# 		align-items: center;
# 	}

# 	#Tabla1 .selectPotencia2 p {
# 		margin-bottom: 0;
# 		margin-right: 10px;
# 		color: #004571;
# 		font-size: 16px;
# 		font-weight: 400;
# 		line-height: 16px;
# 		text-align: center;
# 	}

# 	#Tabla1 .selectPotencia2 .options {
# 		display: none;
# 		margin-top: 5px;
# 		border-top: 1px solid #004571;
# 	}

# 	#Tabla1 .selectPotencia2 .options p {
# 		text-align: left;
# 		margin-top: 8px;
# 	}

# 	#Tabla1 .selectPotencia2 .options p:hover {
# 		color: #e57200;
# 	}

# 	#Tabla1 .tablaPotencia {
# 		background: #f2f5f8;
# 		border-bottom-left-radius: 13.27px;
# 	}

# 	@media screen and (max-width: 768px) {

# 		#Tabla1 .container-switches-icons,
# 		#Tabla1 .container-tabla,
# 		#Tabla1 .container-condiciones-impuestos {
# 			max-width: 90%;
# 		}
# 	}

# 	@media screen and (max-width: 700px) {
# 		#TarifaporUsoGas .container-switches-icons {
# 			flex-direction: column;
# 			align-items: flex-start;
# 			justify-content: flex-start;
# 			gap: 2rem;
# 		}
# 	}


# 	@media screen and (max-width: 400px) {
# #Tabla1.tabla1Class {
#                 overflow-x:scroll !important;
# 	}}

# 	@media screen and (max-width: 600px) {

# 		#Tabla1 .container-switches-icons {
# 			flex-direction: column;
# 			align-items: flex-start;
# 			justify-content: flex-start;
# 			gap: 2rem;
# 		}

#                #Tabla1 .precio{font-size: 12px;
#     line-height: 14px;}
# 	}

# 	@media screen and (max-width: 530px) {
# 		#Tabla1 .selectPotencia2 {
# 			margin-top: -20px;
# 		}

# 		#Tabla1 .tituloIcon-2 {
# 			flex-direction: column;
# 			margin-bottom: 10px;
# 			align-items: flex-start;
# 		}
# 	}

# 	#Tabla1 .faqs-container-modal {
# 		border-bottom: 1px solid #004571;
# 		border-top: 1px solid #004571;
# 		max-width: 768px;
# 		margin: 0 auto;
# 		margin-top: 40px;
# 	}

# 	#Tabla1 .faqs-container-modal .faqs-fila {
# 		display: flex;
# 		cursor: pointer;
# 	}

# 	#Tabla1 .faqs-container-modal .texto-faqs {
# 		width: 87%;
# 		text-align: left;
# 	}

# 	#Tabla1 .faqs-container-modal .img-faqs {
# 		margin-left: 60px;
# 		padding-top: 20px;
# 	}

# 	#Tabla1 p.moreInfo {
# 		margin-top: 20px;
# 		color: #004571 !important;
# 		font-family: 'FSEmeric Semibold', Arial, sans-serif;
# 		font-size: 16px;
# 		margin-bottom: 20px;
# 	}

# 	#Tabla1 .col-faqs p,
# 	#Tabla1 .col-faqs li {
# 		font-family: 'FSEmeric Regular', Arial, sans-serif;
# 	}

# 	@media screen and (max-width: 768px) {
# 		.faqs-container-modal {
# 			max-width: 90%;
# 		}
# 	}

# 	#Tabla1 .logo-selectPotencia {
# 		color: #004571;
# 	}

# 	#Tabla1 .tabla1Class .tExcedentes {
# 		color: #004571;
# 		background-color: #f2f5f8;
# 		margin: auto;
# 		margin-top: 20px;
# 		border: 2px solid #004571;
# 		border-radius: 15px;
# 		padding: 5px;
# 		text-align: center;
# 		max-width: 768px;
# 	}


# 	#Tabla1 .tabla1Class .tExcedentes img {
# 		width: 2.5%;
# 		margin-bottom: 5px;
# 	}

# 	@media screen and (max-width: 768px) {

# 		#Tabla1 .tabla1Class .tExcedentes {
# 			max-width: 90%;
# 		}

# 		#Tabla1 .tabla1Class .tExcedentes img {
# 			width: 6%;
# 		}
# 	}


# 	/* estilos tabla1 */


# 	/* #onetrust-consent-sdk {
#                 display: none;
#             } */
# 	#Tabla1 .container-switches-icons-1,
# 	#Tabla1 .container-tabla-1,
# 	#Tabla1 .container-condiciones-impuestos {
# 		margin: 0 auto;
# 		margin-top: 40px;
# 		display: flex;
# 		max-width: 768px;
# 		align-items: flex-end;
# 		justify-content: space-between;
# 		padding: 10px 10px;
# 		height: auto;
# 	}

# 	#Tabla1 .container-condiciones-impuestos {
# 		margin-top: 20px;
# 		display: flex;
# 		flex-direction: column;
# 		align-items: flex-start;
# 		padding: 0 0;
# 		height: auto;
# 	}

# 	#Tabla1 .container-tabla-1 {
# 		padding: 0 0;
# 	}

# 	#Tabla1 .container-tabla-1 {
# 		border: solid 1px #004571;
# 		border-radius: 13.27px;
# 		border-top-color: transparent;
# 	}

# 	#Tabla1 .tituloIcon1 {
# 		gap: 2rem;
# 		display: flex;
# 		align-items: flex-end;
# 		justify-content: flex-start;
# 	}

# 	#Tabla1 .tituloIcon1 .logo-selectPotencia {
# 		font-weight: 700;
# 	}

# 	#Tabla1 .tituloIcon1 .logo-selectPotencia span {
# 		font-size: 20px;
# 	}

# 	#Tabla1 .tituloIcon .logo-selectPotencia span.icon {
# 		width: 32px;
# 		height: 32px;
# 		color: #e57200;
# 	}

# 	#Tabla1 .switch-button {
# 		display: flex;
# 		align-items: center;
# 	}

# 	#Tabla1 .switch-button p {
# 		font-size: 16px;
# 		font-weight: 400;
# 		line-height: 12px;
# 		margin-bottom: 0;
# 		color: #767676;
# 		line-height: 17px;

# 	}

# 	#Tabla1 .switch {
# 		position: relative;
# 		width: 60px;
# 		margin: 0;
# 		align-items: center;
# 		/*  height: 34px; */
# 	}

# 	#Tabla1 .switch input {
# 		opacity: 0;
# 		width: 0;
# 		height: 0;
# 	}

# 	#Tabla1 .switchIva {
# 		margin-bottom: 10px;
# 	}

# 	#Tabla1 .slider {
# 		position: absolute;
# 		cursor: pointer;
# 		top: 0;
# 		left: 0;
# 		right: 0;
# 		bottom: 0;
# 		background-color: #fff;
# 		-webkit-transition: .4s;
# 		transition: .4s;
# 		border: 2px solid #004571;
# 		border-radius: 10px;
# 		width: 42px;
# 		height: 21px;
# 	}

# 	#Tabla1 .slider:before {
# 		position: absolute;
# 		content: "";
# 		height: 14px;
# 		width: 14px;
# 		left: 2px;
# 		bottom: 2px;
# 		background-color: #9e9e9e;
# 		-webkit-transition: .4s;
# 		transition: .4s;
# 	}

# 	#Tabla1 input:checked+.slider:before {
# 		background-color: #e57200;
# 		/* left: -3px; */
# 	}

# 	#Tabla1 input:checked+.slider {
# 		background-color: #fae2cb;
# 	}

# 	#Tabla1 input:focus+.slider {
# 		box-shadow: 0 0 1px #e57200;
# 	}

# 	#Tabla1 input:checked+.slider:before {
# 		-webkit-transform: translateX(21px);
# 		-ms-transform: translateX(21px);
# 		transform: translateX(21px);
# 	}

# 	#Tabla1 .slider.round {
# 		border-radius: 34px;
# 	}

# 	#Tabla1 .slider.round:before {
# 		border-radius: 50%;
# 	}

# 	#Tabla1 p.pActive {
# 		display: none;
# 	}

# 	#Tabla1 .divPrecios .precio {
# 		color: #004571;
# 		padding: 10px 10px;
# 		font-weight: bold;
# 		display: flex;
# 		text-align: center;
# 		align-items: center;
# 	}

# 	#Tabla1 .infoTarifa .title {
# 		color: #e57200;
# 		font-size: 40px;
# 		font-weight: 400;
# 		line-height: 48px;
# 	}

# 	#Tabla1 .tituloIcon1 p {
# 		color: #004571;
# 		font-size: 32px;
# 		font-weight: 400;
# 		line-height: 39px;
# 		margin-bottom: 0;
# 		margin-left: 15px;
# 	}

# 	#Tabla1 .selectPotencia1 {
# 		cursor: pointer;
# 		border-radius: 19.47px;
# 		padding: 9px 12px;
# 		border: 1px solid #004571;
# 		height: fit-content;
# 		display: grid;
# 		width: fit-content;
# 		margin-top: 35px;
# 	}

# 	#Tabla1 .selectPotencia1.active svg {
# 		transform: rotate(180deg);
# 	}

# 	#Tabla1 .selectPotencia1 .items {
# 		display: flex;
# 		align-items: center;
# 	}

# 	#Tabla1 .selectPotencia1 p {
# 		margin-bottom: 0;
# 		margin-right: 10px;
# 		color: #004571;
# 		font-size: 16px;
# 		font-weight: 400;
# 		line-height: 16px;
# 		text-align: center;
# 	}

# 	#Tabla1 .selectPotencia1 .options {
# 		display: none;
# 		margin-top: 5px;
# 		border-top: 1px solid #004571;
# 	}

# 	#Tabla1 .selectPotencia1 .options p {
# 		text-align: left;
# 		margin-top: 8px;
# 	}

# 	#Tabla1 .selectPotencia1 .options p:hover {
# 		color: #e57200;
# 	}

# 	#Tabla1 .tabla1 .tablaPotencia .titulo,
# 	#Tabla1 .tabla1 .tablaEnergia .titulo {
# 		text-align: center;
# 		background: #004571;
# 		color: #fff;
# 		padding: 15px 10px;
# 	}

# 	#Tabla1 .tabla1 .tablaPotencia .titulo {
# 		border-top-left-radius: 13.27px;
# 		border-right: 1px solid #407495;
# 	}

# 	#Tabla1 .tabla1 .tablaEnergia .titulo {
# 		border-top-right-radius: 13.27px;
# 	}

# 	#Tabla1 .tabla1 {
# 		display: grid;
# 		grid-template-columns: 2fr 1fr;
# 	}

# 	#Tabla1 .tabla1 .divHorarios {
# 		height: 120px;
# 	}

# 	#Tabla1 .tabla1 .tablaEnergia .container-div-horarios-precios,
# 	#Tabla1 .tabla1 .tablaPotencia .container-div-horarios-precios {
# 		display: flex;
# 		align-items: center;
# 		justify-content: center;
# 		flex-direction: column;
# 	}

# 	#Tabla1 .tabla1 .tablaEnergia .divHorarios,
# 	#Tabla1 .tabla1 .tablaPotencia .divHorarios {
# 		background: #f2f5f8;
# 		color: #004571;
# 		font-size: 14px;
# 		font-weight: 400;
# 		line-height: 20px;
# 		text-align: center;
# 		justify-content: center;
# 		display: flex;
# 	}

# 	#Tabla1 .tabla1 .tablaEnergia .divPrecios,
# 	#Tabla1 .tabla1 .tablaPotencia .divPrecios {
# 		display: flex;
# 		align-items: center;
# 		justify-content: center;
# 		font-size: 14px;
# 	}

# 	#Tabla1 .tabla1 .tablaPotencia .divHorarios {
# 		display: grid;
# 		grid-template-columns: 1fr 1fr;
# 		place-items: center;
# 		text-align: center;
# 	}

# 	#Tabla1 .tabla1 .tablaPotencia .divPrecios {
# 		font-weight: 400;
# 		line-height: 20px;
# 		display: grid;
# 		grid-template-columns: 1fr 1fr;
# 		place-items: center;
# 		text-align: center;
# 		width: 100%;
# 		background: white;
# 		border-bottom-left-radius: 13.27px;
# 	}

# 	#Tabla1 .tabla1 .tablaPotencia .textH,
# 	#Tabla1 .tabla1 .tablaEnergia .textH {
# 		height: 100%;
# 		width: 100%;
# 		display: flex;
# 		justify-content: center;
# 	}

# 	#Tabla1 .tabla1 .tablaPotencia .textH {
# 		border-right: 1px solid #407495;
# 	}

# 	#Tabla1 .tabla1 .tablaPotencia .textH .horario,
# 	#Tabla1 .tabla1 .tablaEnergia .textH .horario {
# 		padding: 30px 20px;
# 	}

# 	#Tabla1 .container-condiciones-impuestos .text-container-condiciones-impuestos {
# 		font-size: 12px;
# 	}

# 	@media screen and (max-width: 768px) {

# 		#Tabla1 .container-switches-icons-1,
# 		#Tabla1 .container-tabla-1,
# 		#Tabla1 .container-condiciones-impuestos {
# 			/*max-width: 90%;*/
# 		}

# 		#Tabla1 .faqs-container-modal {
# 			max-width: 90%;
# 		}
# 	}

# 	@media screen and (max-width: 720px) {
# 		#Tabla1 .container-switches-icons-1 {
# 			flex-direction: column;
# 			align-items: flex-start;
# 			justify-content: flex-start;
# 			gap: 2rem;
# 		}
# 	}

# 	@media screen and (max-width: 670px) {
# 		#Tabla1 .tabla1 {
# 			grid-template-columns: 1fr;
# 			border: none;
# 		}

# 		#Tabla1 .tabla1 .tablaPotencia {
# 			border: 1px solid #407495;
# 			border-radius: 13.27px;
# 			margin-bottom: 20px;
# 		}

# 		#Tabla1 .tabla1 .tablaPotencia .titulo {
# 			border-top-right-radius: 13.27px;
# 		}

# 		#Tabla1 .tabla1 .tablaPotencia .textH:nth-child(2) {
# 			border-right: none;
# 		}

# 		#Tabla1 .tabla1 .tablaPotencia .divPrecios {
# 			border-bottom-right-radius: 13.27px;
# 		}

# 		#Tabla1 .tabla1 .tablaEnergia .titulo {
# 			border-top-left-radius: 13.27px;
# 		}

# 		#Tabla1 .tabla1 .tablaEnergia .divHorarios {
# 			width: 100%;
# 			height: auto !important;

# 		}

# 		#Tabla1 .tabla1 .tablaEnergia .container-div-horarios-precios {
# 			border: 1px solid #407495;
# 			border-bottom-right-radius: 13.27px;
# 			border-bottom-left-radius: 13.27px;
# 		}
# 	}

# 	@media screen and (max-width: 414px) {
# 		#Tabla1 .selectPotencia1 {
# 			margin-top: -20px;
# 		}

# 		#Tabla1 .tituloIcon1 {
# 			flex-direction: column;
# 			margin-bottom: 10px;
# 			align-items: flex-start;
# 		}

# 		#Tabla1 .tabla1 .tablaPotencia .textH .horario,
# 		#Tabla1 .tabla1 .tablaEnergia .textH .horario {
# 			padding: 10px 20px;
# 		}
# 	}

# 	@media screen and (max-width: 550px) {

# 		#Tabla1 .tabla1 .tablaPotencia .textH .horario,
# 		#Tabla1 .tabla1 .tablaEnergia .textH .horario {
# 			padding: 20px 20px;
# 		}

# 		#Tabla1 .tabla1 .divHorarios {
# 			height: auto;
# 		}

# 	}

# 	#Tabla1 .faqs-container-modal {
# 		border-bottom: 1px solid #004571;
# 		border-top: 1px solid #004571;
# 		max-width: 768px;
# 		margin: 0 auto;
# 		margin-top: 40px;
# 	}

# 	#Tabla1 .faqs-container-modal .faqs-fila {
# 		display: flex;
# 		cursor: pointer;
# 	}

# 	#Tabla1 .faqs-container-modal .texto-faqs {
# 		width: 87%;
# 		text-align: left;
# 	}

# 	#Tabla1 .faqs-container-modal .img-faqs {
# 		margin-left: 60px;
# 		padding-top: 20px;
# 	}

# 	#Tabla1 p.moreInfo {
# 		margin-top: 20px;
# 		color: #004571 !important;
# 		font-family: 'FSEmeric Semibold', Arial, sans-serif;
# 		font-size: 16px;
# 		margin-bottom: 20px;
# 	}

# 	#Tabla1 .col-faqs p,
# 	#Tabla1 .col-faqs li {
# 		font-family: 'FSEmeric Regular', Arial, sans-serif;
# 	}

# 	@media screen and (max-width: 768px) {
# 		#Tabla1 .faqs-container-modal {
# 			max-width: 90%;
# 		}
# 	}

# 	#Tabla1 .logo-selectPotencia {
# 		color: #004571;
# 	}

# 	#Tabla1 .container-switches-icons,
# 	#Tabla1 .container-tabla,
# 	#Tabla1 .container-condiciones-impuestos {
# 		margin-top: 0;
# 	}
# </style>


#         <div id="Tabla1" style="margin-bottom: 40px; display: block;" class="tabla1Class id-1615692614551">

#             <div class="container-switches-icons">
#                 <!-- Selector de Potencias + Iconos  -->
#                 <div class="tituloIcon-2">
#                     <!-- Icon + Text -->
#                     <div class="logo-selectPotencia">
#                         <span class="icon icon-luz-rv" style="color:#e57200; font-size:32px"></span>
#                         <span>Luz</span>
#                     </div>


#                     <!-- Selector de Potencia -->


#                     <div class="selectPotencia2" data-assetid="1615692614551">
#                         <div class="selectDefault">
#                             <div class="items">

#                                 <p class="defaultOption" data-assetid="1615692614551">Potencia 10-15kW</p><svg width="10px" height="6px" viewBox="0 0 10 6" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
#                                             <g id="Group-29-Copy-2" transform="translate(0.76416016 0.76416016)">
#                                                 <path d="M0 0L2.19765 1.911L4.3953 3.822" transform="matrix(1.1924881E-08 1 -1 1.1924881E-08 7.644 -5.9604645E-08)" id="Line" fill="none" fill-rule="evenodd" stroke="#004571" stroke-width="1.5288001" stroke-linecap="round"></path>
#                                                 <path d="M0 3.822L4.3953 0" transform="matrix(1.1924881E-08 1 -1 1.1924881E-08 3.8220003 -5.9604645E-08)" id="Line" fill="none" fill-rule="evenodd" stroke="#004571" stroke-width="1.5288001" stroke-linecap="round"></path>
#                                             </g>
#                                         </svg></div>
#                         </div>


#                             <div class="options" style="display: none;">


#                                                         <p class="defaultOption">Potencia ≤10kW</p>


#                                                         <p class="defaultOption">Potencia 10-15kW</p>


#                                 </div></div>
#                 </div>
#                 <!-- SWITCHES -->

#                     <div class="switches">

#                             <div class="switch-button switchIva" data-assetid="1615692614551">
#                                 <label class="switch"><input type="checkbox" data-assetid="1615692614551"><span class="slider-2 round iva"></span></label><p class="pActive" style="color: rgb(0, 69, 113); display: none;">Precios con impuestos</p><p class="pNoActive" style="color: rgb(0, 69, 113); display: block;">Precios sin impuestos</p></div>


#                     </div>

#             </div>


#             <div class="container-tabla-1 tabla1">


#         <div class="tablaPotencia" data-table="p1" data-algo="0" data-typevalor="NO IVA" data-potencia="Potencia ≤10kW" data-assetid="1615692614551" style="display: none;"><div class="titulo">Término de potencia</div><div class="container-div-horarios-precios"><div class="divHorarios">
#                                 <div class="textH">
#                                     <div class="horario">De 08h a 00h (de lunes a viernes) Período Punta (P1)</div>
#                                 </div>
#                                 <div class="textH">
#                                     <div class="horario">De 00h a 08h (de lunes a viernes) y las 24h (fines de semana y festivos) Período Valle (P2)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: none;" data-table="p1" data-algo="0" data-typevalor="NO IVA" data-potencia="Potencia ≤10kW" data-assetid="1615692614551"><div class="textH"><div class="precio">0,103663€/kW*día</div></div><!-- 5 --><div class="textH"><div class="precio">0,034042€/kW*día</div></div><!-- 5 --></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --><div class="tablaEnergia" data-table="p1" data-algo="2" data-typevalor="NO IVA" data-potencia="Potencia ≤10kW" data-assetid="1615692614551" style="display: none;"><div class="titulo">Término de energía</div><div class="container-div-horarios-precios"><div class="divHorarios" style="height: 120px;">
#                                 <div class="textH">
#                                     <div class="horario">Mismo precio 24h (de lunes a viernes, fines de semana y festivos)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: none;" data-table="p1" data-algo="2" data-typevalor="NO IVA" data-potencia="Potencia ≤10kW" data-assetid="1615692614551"><div class="textH"><div class="precio">0,114900€/kWh</div></div><!-- 5 --></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --><div class="tablaPotencia" data-table="p1" data-algo="3" data-typevalor="IVA" data-potencia="Potencia ≤10kW" data-assetid="1615692614551" style="display: none;"><div class="titulo">Término de potencia</div><div class="container-div-horarios-precios"><div class="divHorarios">
#                                 <div class="textH">
#                                     <div class="horario">De 08h a 00h (de lunes a viernes) Período Punta (P1)</div>
#                                 </div>
#                                 <div class="textH">
#                                     <div class="horario">De 00h a 08h (de lunes a viernes) y las 24h (fines de semana y festivos) Período Valle (P2)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: none;" data-table="p1" data-algo="3" data-typevalor="IVA" data-potencia="Potencia ≤10kW" data-assetid="1615692614551"><div class="textH"><div class="precio">0,131845€/kW*día</div></div><!-- 5 --><div class="textH"><div class="precio">0,043297€/kW*día</div></div><!-- 5 --></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --><div class="tablaEnergia" data-table="p1" data-algo="5" data-typevalor="IVA" data-potencia="Potencia ≤10kW" data-assetid="1615692614551" style="display: none;"><div class="titulo">Término de energía</div><div class="container-div-horarios-precios"><div class="divHorarios" style="height: 120px;">
#                                 <div class="textH">
#                                     <div class="horario">Mismo precio 24h (de lunes a viernes, fines de semana y festivos)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: none;" data-table="p1" data-algo="5" data-typevalor="IVA" data-potencia="Potencia ≤10kW" data-assetid="1615692614551"><div class="textH"><div class="precio">0,146137€/kWh</div></div><!-- 5 --></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --><div class="tablaPotencia" data-table="p1" data-algo="6" data-typevalor="NO IVA DESCUENTO" data-potencia="Potencia ≤10kW" data-assetid="1615692614551" style="display: none;"><div class="titulo">Término de potencia</div><div class="container-div-horarios-precios"><div class="divHorarios">
#                                 <div class="textH">
#                                     <div class="horario">De 08h a 00h (de lunes a viernes) Período Punta (P1)</div>
#                                 </div>
#                                 <div class="textH">
#                                     <div class="horario">De 00h a 08h (de lunes a viernes) y las 24h (fines de semana y festivos) Período Valle (P2)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: none;" data-table="p1" data-algo="6" data-typevalor="NO IVA DESCUENTO" data-potencia="Potencia ≤10kW" data-assetid="1615692614551"></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --><div class="tablaEnergia" data-table="p1" data-algo="8" data-typevalor="NO IVA DESCUENTO" data-potencia="Potencia ≤10kW" data-assetid="1615692614551" style="display: none;"><div class="titulo">Término de energía</div><div class="container-div-horarios-precios"><div class="divHorarios" style="height: 120px;">
#                                 <div class="textH">
#                                     <div class="horario">Mismo precio 24h (de lunes a viernes, fines de semana y festivos)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: none;" data-table="p1" data-algo="8" data-typevalor="NO IVA DESCUENTO" data-potencia="Potencia ≤10kW" data-assetid="1615692614551"></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --><div class="tablaPotencia" data-table="p1" data-algo="9" data-typevalor="IVA DESCUENTO" data-potencia="Potencia ≤10kW" data-assetid="1615692614551" style="display: none;"><div class="titulo">Término de potencia</div><div class="container-div-horarios-precios"><div class="divHorarios">
#                                 <div class="textH">
#                                     <div class="horario">De 08h a 00h (de lunes a viernes) Período Punta (P1)</div>
#                                 </div>
#                                 <div class="textH">
#                                     <div class="horario">De 00h a 08h (de lunes a viernes) y las 24h (fines de semana y festivos) Período Valle (P2)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: none;" data-table="p1" data-algo="9" data-typevalor="IVA DESCUENTO" data-potencia="Potencia ≤10kW" data-assetid="1615692614551"></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --><div class="tablaEnergia" data-table="p1" data-algo="11" data-typevalor="IVA DESCUENTO" data-potencia="Potencia ≤10kW" data-assetid="1615692614551" style="display: none;"><div class="titulo">Término de energía</div><div class="container-div-horarios-precios"><div class="divHorarios" style="height: 120px;">
#                                 <div class="textH">
#                                     <div class="horario">Mismo precio 24h (de lunes a viernes, fines de semana y festivos)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: none;" data-table="p1" data-algo="11" data-typevalor="IVA DESCUENTO" data-potencia="Potencia ≤10kW" data-assetid="1615692614551"></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" -->


#         <div class="tablaPotencia" data-table="p2" data-algo="0" data-typevalor="NO IVA" data-potencia="Potencia 10-15kW" data-assetid="1615692614551" style="display: grid;"><div class="titulo">Término de potencia</div><div class="container-div-horarios-precios"><div class="divHorarios">
#                                 <div class="textH">
#                                     <div class="horario">De 08h a 00h (de lunes a viernes) Período Punta (P1)</div>
#                                 </div>
#                                 <div class="textH">
#                                     <div class="horario">De 00h a 08h (de lunes a viernes) y las 24h (fines de semana y festivos) Período Valle (P2)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: grid;" data-table="p2" data-algo="0" data-typevalor="NO IVA" data-potencia="Potencia 10-15kW" data-assetid="1615692614551"><div class="textH"><div class="precio">0,103663€/kW*día</div></div><!-- 5 --><div class="textH"><div class="precio">0,034042€/kW*día</div></div><!-- 5 --></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --><div class="tablaEnergia" data-table="p2" data-algo="2" data-typevalor="NO IVA" data-potencia="Potencia 10-15kW" data-assetid="1615692614551" style="display: grid;"><div class="titulo">Término de energía</div><div class="container-div-horarios-precios"><div class="divHorarios" style="height: 120px;">
#                                 <div class="textH">
#                                     <div class="horario">Mismo precio 24h (de lunes a viernes, fines de semana y festivos)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: grid;" data-table="p2" data-algo="2" data-typevalor="NO IVA" data-potencia="Potencia 10-15kW" data-assetid="1615692614551"><div class="textH"><div class="precio">0,114900€/kWh</div></div><!-- 5 --></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --><div class="tablaPotencia" data-table="p2" data-algo="3" data-typevalor="IVA" data-potencia="Potencia 10-15kW" data-assetid="1615692614551" style="display: none;"><div class="titulo">Término de potencia</div><div class="container-div-horarios-precios"><div class="divHorarios">
#                                 <div class="textH">
#                                     <div class="horario">De 08h a 00h (de lunes a viernes) Período Punta (P1)</div>
#                                 </div>
#                                 <div class="textH">
#                                     <div class="horario">De 00h a 08h (de lunes a viernes) y las 24h (fines de semana y festivos) Período Valle (P2)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: none;" data-table="p2" data-algo="3" data-typevalor="IVA" data-potencia="Potencia 10-15kW" data-assetid="1615692614551"><div class="textH"><div class="precio">0,131845€/kW*día</div></div><!-- 5 --><div class="textH"><div class="precio">0,043297€/kW*día</div></div><!-- 5 --></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --><div class="tablaEnergia" data-table="p2" data-algo="5" data-typevalor="IVA" data-potencia="Potencia 10-15kW" data-assetid="1615692614551" style="display: none;"><div class="titulo">Término de energía</div><div class="container-div-horarios-precios"><div class="divHorarios" style="height: 120px;">
#                                 <div class="textH">
#                                     <div class="horario">Mismo precio 24h (de lunes a viernes, fines de semana y festivos)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: none;" data-table="p2" data-algo="5" data-typevalor="IVA" data-potencia="Potencia 10-15kW" data-assetid="1615692614551"><div class="textH"><div class="precio">0,146137€/kWh</div></div><!-- 5 --></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --><div class="tablaPotencia" data-table="p2" data-algo="6" data-typevalor="NO IVA DESCUENTO" data-potencia="Potencia 10-15kW" data-assetid="1615692614551" style="display: none;"><div class="titulo">Término de potencia</div><div class="container-div-horarios-precios"><div class="divHorarios">
#                                 <div class="textH">
#                                     <div class="horario">De 08h a 00h (de lunes a viernes) Período Punta (P1)</div>
#                                 </div>
#                                 <div class="textH">
#                                     <div class="horario">De 00h a 08h (de lunes a viernes) y las 24h (fines de semana y festivos) Período Valle (P2)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: none;" data-table="p2" data-algo="6" data-typevalor="NO IVA DESCUENTO" data-potencia="Potencia 10-15kW" data-assetid="1615692614551"></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --><div class="tablaEnergia" data-table="p2" data-algo="8" data-typevalor="NO IVA DESCUENTO" data-potencia="Potencia 10-15kW" data-assetid="1615692614551" style="display: none;"><div class="titulo">Término de energía</div><div class="container-div-horarios-precios"><div class="divHorarios" style="height: 120px;">
#                                 <div class="textH">
#                                     <div class="horario">Mismo precio 24h (de lunes a viernes, fines de semana y festivos)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: none;" data-table="p2" data-algo="8" data-typevalor="NO IVA DESCUENTO" data-potencia="Potencia 10-15kW" data-assetid="1615692614551"></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --><div class="tablaPotencia" data-table="p2" data-algo="9" data-typevalor="IVA DESCUENTO" data-potencia="Potencia 10-15kW" data-assetid="1615692614551" style="display: none;"><div class="titulo">Término de potencia</div><div class="container-div-horarios-precios"><div class="divHorarios">
#                                 <div class="textH">
#                                     <div class="horario">De 08h a 00h (de lunes a viernes) Período Punta (P1)</div>
#                                 </div>
#                                 <div class="textH">
#                                     <div class="horario">De 00h a 08h (de lunes a viernes) y las 24h (fines de semana y festivos) Período Valle (P2)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: none;" data-table="p2" data-algo="9" data-typevalor="IVA DESCUENTO" data-potencia="Potencia 10-15kW" data-assetid="1615692614551"></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --><div class="tablaEnergia" data-table="p2" data-algo="11" data-typevalor="IVA DESCUENTO" data-potencia="Potencia 10-15kW" data-assetid="1615692614551" style="display: none;"><div class="titulo">Término de energía</div><div class="container-div-horarios-precios"><div class="divHorarios" style="height: 120px;">
#                                 <div class="textH">
#                                     <div class="horario">Mismo precio 24h (de lunes a viernes, fines de semana y festivos)</div>
#                                 </div>
#                             </div><div class="divPrecios" style="height: 72px; display: none;" data-table="p2" data-algo="11" data-typevalor="IVA DESCUENTO" data-potencia="Potencia 10-15kW" data-assetid="1615692614551"></div><!-- divPrecios--></div><!-- 4 --></div><!-- div class="container-div-horarios-precios" --></div><!-- 2 -->


#         </div>


#    <!--      <script>
#             $(document).ready(function(){
#                 elementos = $("#Tabla1 .precio");
#                 texto ="";
#                 setTimeout(function(){
#                     elementos.each(function () {
#                         texto = $(this).text();

#                         var textoModificado = completarDecimales(texto);
#                         console.log(textoModificado);

#                         $(this).text(textoModificado);

#                     });
#                 },3000)
#             });

#             function reemplazar(match, decimal, unidad) {
#                 console.log('reemplazar')
#                 var decimalComoTexto = decimal.replace(',', '.');
#                 var decimalComoNumero = parseFloat(decimalComoTexto);
#                 var decimalFormateado = decimalComoNumero.toFixed(6);
#                 decimalFormateado = decimalFormateado.replace('.', ',');
#                 decimalFormateado_ = decimalFormateado + unidad;
#                 return decimalFormateado_;
#             }

#             function completarDecimales(texto) {
#                 console.log('completar')
#                 var regex = /(\d+,\d{4})(â¬\/kWh)/g;

#                 while (regex.test(texto)) {
#                     texto = texto.replace(regex, reemplazar);
#                 }

#                 return texto;
#             }


#         </script> -->


# <style type="text/css">#Tabla1 {
#       overflow-x: initial;
#    }
# </style>

#                                                                 </div>
#                                                             </div>
#                                                   </div>


#                                           <script>
#                                             $(document).ready(function(){
#                                                     var titlePage = $(document).attr("title");
#                                                     $('.tog-faq2-1615661140557').click(function() {

#                                                         if($('.moreInfoDetail2-1615661140557').css('display') == 'none'){

#                                                             $('.tog-faq2-1615661140557 svg').css({'transform': 'rotate(-180deg)'});

#                                                         }else{

#                                                             $('.tog-faq2-1615661140557 svg').css({'transform': 'rotate(-360deg)'});
#                                                         }

#                                                         $('.moreInfoDetail2-1615661140557').toggle('slow');

#                                                     });
#                                             });
#                                           </script>
#                                                   <div class="faqs-container">


# 																<div class="faqs-fila tog-faq2-1615661140557" onclick="javascript:dataLayer.push({'event':'event.naturgy','eventCategory':'desplegable','eventAction': 'saber mas','eventLabel':'GNF - Tarifa Por Uso Luz - Condiciones de aplicación de impuestos y otros conceptos regulados'});">


#                                                                   <div class="texto-faqs">
#                                                                       <p class="moreInfo">Condiciones de aplicación de impuestos y otros conceptos regulados</p>
#                                                                   </div>

#                                                                   <div class="img-faqs">
#                                                                             <svg width="16" height="10" viewBox="0 0 16 10" fill="none" xmlns="http://www.w3.org/2000/svg" style="transform: rotate(-180deg);">
#                                                                                 <path d="M7.90362 8.80881C7.90319 8.80856 7.90278 8.80831 7.90238 8.80807L7.8916 8.80175L7.8909 8.80128L7.88576 8.79816C7.87486 8.78748 7.86391 8.77768 7.85319 8.76874C7.84622 8.76209 7.83996 8.75642 7.83474 8.75181C7.83396 8.75112 7.83319 8.75044 7.83242 8.74977L0.559323 0.871814L0.559088 0.871559C0.47633 0.782044 0.481023 0.641484 0.569942 0.557569C0.654991 0.477306 0.785344 0.481 0.866273 0.568536L7.63399 7.89873L8.00144 8.29673L8.3688 7.89865L15.1322 0.569719C15.2144 0.482661 15.3489 0.481614 15.4296 0.557569C15.5199 0.642744 15.522 0.786693 15.4435 0.871703L15.4434 0.871819L8.17344 8.74658C8.17268 8.74725 8.17191 8.74793 8.17112 8.74862C8.16508 8.75397 8.15764 8.76073 8.14933 8.76877C8.1439 8.77333 8.13786 8.77857 8.13137 8.78451C8.12427 8.79057 8.11718 8.79613 8.11101 8.8006L8.10167 8.80584C8.09773 8.80805 8.09272 8.8106 8.08074 8.81613L8.07444 8.8174L8.04375 8.82903L8.03307 8.83175L8.03256 8.83188C8.02672 8.83284 8.02127 8.83372 8.01585 8.83457L8.01572 8.83457L8.00577 8.83459C8.00452 8.83451 8.00266 8.83439 8.0001 8.83421L7.99885 8.83412C7.99399 8.83378 7.98478 8.83314 7.97527 8.83262C7.9648 8.83021 7.95869 8.8286 7.95429 8.8273C7.94635 8.82442 7.93929 8.82201 7.93338 8.82007C7.92742 8.81812 7.92175 8.81634 7.91743 8.81501C7.91109 8.81232 7.90671 8.81031 7.90362 8.80881Z" fill="#004571" stroke="#004571" path="">
#                                                                                     </path>
#                                                                             </svg>
#                                                                         </div>
#                                                             </div>
#                                                             <div class="moreInfoDetail2-1615661140557" style="">
#                                                                 <div class="col-faqs">
#                                                                   <p>Se aplicarán en el precio indicado las variaciones al alza o a la baja de los impuestos aplicables y de los conceptos regulados (a modo enunciativo no limitativo, cargos del sistema, peajes, alquiler de contador...). Asimismo, podrán trasladarse al precio cualquier concepto regulado, tasa o impuesto de nueva creación o que sustituyan a los actuales que sean de aplicación durante el periodo de duración del presente contrato.</p>

# <p>Según indica Real Decreto-ley 8/2023 los precios incluyen IVA bajo las siguientes condiciones para potencias contratadas inferiores o iguales a 10kW:</p>

# <ol>
# 	<li>Hasta el 31/12/2024 cuando el precio medio de la energía del mercado mayorista del último mes natural anterior al del último día del periodo de facturación supere los 45 €/MWh se aplicará IVA reducido del 10%.</li>
# 	<li>Cuando el precio medio de la energía del mercado mayorista del último mes natural anterior al del último día del periodo de facturación sea inferior a los 45 €/MWh se aplicará el IVA del 21%.</li>
# 	<li>Hasta el 30/06/2024 se aplicará el 3,8% del Impuesto Especial sobre electricidad (IEE).</li>
# </ol>

# <p>Los precios con impuestos se les ha aplicado un IEE de un 5,1127% y un IVA del 21%. En cualquier caso, se aplicarán los impuestos establecidos en cada momento por la regulación vigente.</p>

# <p>En lugar de IVA, en Canarias se aplica el IGIC y para Ceuta y Melilla aplica el IPSI correspondiente.</p>

# <p>Los precios no incluyen el coste regulado asociado al mecanismo de financiación del bono social, que se añadirá en línea aparte bajo el concepto “Financiación del Bono Social”.</p>

#                                                                 </div>
#                                                             </div>
#                                                   </div>


#                                           <script>
#                                             $(document).ready(function(){
#                                                     var titlePage = $(document).attr("title");
#                                                     $('.tog-faq3-1615613000504').click(function() {

#                                                         if($('.moreInfoDetail3-1615613000504').css('display') == 'none'){

#                                                             $('.tog-faq3-1615613000504 svg').css({'transform': 'rotate(-180deg)'});

#                                                         }else{

#                                                             $('.tog-faq3-1615613000504 svg').css({'transform': 'rotate(-360deg)'});
#                                                         }

#                                                         $('.moreInfoDetail3-1615613000504').toggle('slow');

#                                                     });
#                                             });
#                                           </script>
#                                                   <div class="faqs-container">


# 																<div class="faqs-fila tog-faq3-1615613000504" onclick="javascript:dataLayer.push({'event':'event.naturgy','eventCategory':'desplegable','eventAction': 'saber mas','eventLabel':'GNF - Tarifa Por Uso Luz - Condiciones de la oferta'});">


#                                                                   <div class="texto-faqs">
#                                                                       <p class="moreInfo">Condiciones de la oferta</p>
#                                                                   </div>

#                                                                   <div class="img-faqs">
#                                                                             <svg width="16" height="10" viewBox="0 0 16 10" fill="none" xmlns="http://www.w3.org/2000/svg" style="transform: rotate(-360deg)">
#                                                                                 <path d="M7.90362 8.80881C7.90319 8.80856 7.90278 8.80831 7.90238 8.80807L7.8916 8.80175L7.8909 8.80128L7.88576 8.79816C7.87486 8.78748 7.86391 8.77768 7.85319 8.76874C7.84622 8.76209 7.83996 8.75642 7.83474 8.75181C7.83396 8.75112 7.83319 8.75044 7.83242 8.74977L0.559323 0.871814L0.559088 0.871559C0.47633 0.782044 0.481023 0.641484 0.569942 0.557569C0.654991 0.477306 0.785344 0.481 0.866273 0.568536L7.63399 7.89873L8.00144 8.29673L8.3688 7.89865L15.1322 0.569719C15.2144 0.482661 15.3489 0.481614 15.4296 0.557569C15.5199 0.642744 15.522 0.786693 15.4435 0.871703L15.4434 0.871819L8.17344 8.74658C8.17268 8.74725 8.17191 8.74793 8.17112 8.74862C8.16508 8.75397 8.15764 8.76073 8.14933 8.76877C8.1439 8.77333 8.13786 8.77857 8.13137 8.78451C8.12427 8.79057 8.11718 8.79613 8.11101 8.8006L8.10167 8.80584C8.09773 8.80805 8.09272 8.8106 8.08074 8.81613L8.07444 8.8174L8.04375 8.82903L8.03307 8.83175L8.03256 8.83188C8.02672 8.83284 8.02127 8.83372 8.01585 8.83457L8.01572 8.83457L8.00577 8.83459C8.00452 8.83451 8.00266 8.83439 8.0001 8.83421L7.99885 8.83412C7.99399 8.83378 7.98478 8.83314 7.97527 8.83262C7.9648 8.83021 7.95869 8.8286 7.95429 8.8273C7.94635 8.82442 7.93929 8.82201 7.93338 8.82007C7.92742 8.81812 7.92175 8.81634 7.91743 8.81501C7.91109 8.81232 7.90671 8.81031 7.90362 8.80881Z" fill="#004571" stroke="#004571" path="">
#                                                                                     </path>
#                                                                             </svg>
#                                                                         </div>
#                                                             </div>
#                                                             <div class="moreInfoDetail3-1615613000504" style="display: none;">
#                                                                 <div class="col-faqs">
#                                                                   <p><strong>Luz</strong></p>

# <p>Oferta para nuevas contrataciones de luz con tarifa de acceso 2.0TD para persona física, potencia contratada ≤ 15 kW, consumo de electricidad hasta 10.000 kWh/año y sin Bono Social. Las condiciones se mantendrán vigentes 12 meses desde el inicio de vigencia del contrato. Tarifa sin permanencia.<br>
# <br>
# Vigencia hasta el <span class="fechaTarifaPorUso">31/08/2024</span>&nbsp;y no acumulable a otras promociones.</p>

# <p><strong>Gas</strong></p>

# <p>Oferta para nuevas contrataciones de de gas con tarifas ATR RL1, RL2 y RL3 para persona física. Tarifa sin permanencia.<br>
# <br>
# Oferta vigente hasta el <span class="fechaTarifaPorUso">31/08/2024</span>&nbsp;y no acumulable a otras promociones.&nbsp;</p>

# <p><span class="icon icon-pdf" style="color:#004571; font-size:10px"></span>&nbsp;<a href="https://www.naturgy.es/files/0522_Condiciones_Generales_ES.pdf" onclick="dataLayer.push({'event':'callToAction','eventAction':'descargar','eventLabel':'H - Tarifa por uso luz - precios - condiciones generales'})"><u>Condiciones generales del contrato</u></a></p>

#                                                                 </div>
#                                                             </div>
#                                                   </div>


# </div>

# <style>
# .col-faqs{font-family: 'FSEmeric Regular', Arial, sans-serif;color: #004571;}
# .col-faqs p, .col-faqs li {
#     font-family: 'FSEmeric Regular', Arial, sans-serif !important;
# }
# </style>


#             </div>
#             </div>
