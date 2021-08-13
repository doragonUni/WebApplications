#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
from datetime import datetime
import sys
import os
from io import TextIOWrapper

import filetype

from database import Avistamientos

# print("Content-type: text/html;charset=UTF-8\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

# avistamientoDB = Avistamientos("localhost", "root", "", "tarea2")
avistamientoDB = Avistamientos("localhost", "cc500246_u", "squeegetni", "cc500246_db")
data = avistamientoDB.get_last5()  # tenemos la data

head = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Portada</title>

   <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="shortcut icon" type="image/x-icon" href="docs/images/favicon.ico" />
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>

  <link rel="title icon" href="../titleicon.png"/>

  <style>
    .title {
      margin-left: 20%;
      margin-top: 5%;
    }

    body {
      background-color: rgb(238, 226, 208);
      font-family: "Helvetica";
      color: rgb(115, 54, 54);
    }

    header{
      margin-top: 0;
    }

    table, th, td {
      border: 1px solid black;
      border-collapse: collapse;
      text-align: left;
      padding: 8px;
      margin-bottom: 10%;
    }

    td img {
      display: block;
      object-fit: scale-down;
    }

    .table {
      width: 60%;
      margin-left: auto;
      margin-right: auto;
      color: black;

    }

    .table-title {
      margin-left: 20%;
    }

    .ultimos-avistamientos {
      margin-top: 5%;
    }

    .topBar {
      margin-top: 0;
      margin-left: 0;
      overflow: hidden;
      background-color: rgb(91, 124, 91);

    }

    .topBar img {
      display: inline-block;
      object-fit: scale-down;

    }

    .topBar nav{
      margin-left: 40px;
    }

    .topBar a {
      text-align: center;
      padding: 40px;
      font-size: 24px;
      color: rgb(238, 226, 208);
      text-decoration: none;
    }

    .topBar a:hover {
      background-color: rgb(115, 54, 54);
      color: rgb(238, 226, 208);
    }
    .foto {
      width: 120px;
      height: 120px;
    }

    #mapid { height: 180px; }

  </style>

</head>
'''

print(head, file=utf8stdout)

header = f'''
<body>
<header>
  <div class="topBar">
    <nav>
      <img alt="abeja para la pagina" src="../pageicon1.png">
      <a href="../avistamientos.html">Informar un avistamiento</a>
      <a href="listaAvistamientos.py?page=0">Ver Listado</a>
      <a href="../Grafico.html">Ver Gráficos</a>
    </nav>

  </div>
</header>
'''

print(header, file=utf8stdout)

table_header = f'''
<div class="title"><h1>Sistema de reportes de insectos!</h1></div>


<div class="ultimos-avistamientos">
  <h2 class="table-title">Ultimos avistamientos</h2>
  <table class="table">
    <thead>
    <tr>
      <th>Fecha-Hora</th>
      <th>Comuna</th>
      <th>Sector</th>
      <th>Tipo</th>
      <th>Foto</th>
    </tr>
    </thead>
'''

print(table_header, file=utf8stdout)

for d in data:
  photo = avistamientoDB.get_photo(d[4])[0][0]  # primer 0 determina la ultima foto, 1 pa la siguiente y asi...
  row = f'''
          <tbody>
            <tr>
                <th>{str(d[0])}</th>
                <th>{str(d[1])}</th>
                <th>{str(d[2])}</th>
                <th>{str(d[3])}</th>
                <th><img class="foto" alt="photo" src="../media/{str(photo)}"> </th>
            </tr>
    '''
  print(row, file=utf8stdout)

table_footer = '''
  </tbody>
  </table>
  </div>
  '''
print(table_footer, file=utf8stdout)

map = '''
  <div id="mapid" style="margin: auto; width: 600px; height: 400px;"></div>

<script>
    let xhr = new XMLHttpRequest();
    xhr.open('POST', 'markersMap.py');
    xhr.send();
    xhr.timeout = 5000;
    xhr.onload = function (data) {

        let coordenadasJson = JSON.parse(data.currentTarget.responseText);
        console.log(coordenadasJson)
        let comunas = Object.keys(coordenadasJson);
        let coordenadas = Object.values(coordenadasJson);

        var mymap = L.map('mapid').setView([-33.45, -70.66], 13);

        L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v9',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'pk.eyJ1IjoiZG9yYWdvbiIsImEiOiJja3BsdWNrd3kwenQwMnZwYTQ5emh5NnlnIn0.ocelY3F5aLMlsuJYffRMjw'
        }).addTo(mymap);

	    for (let i = 0; i< comunas.length; i++) {
               let comuna = comunas[i];
               let lat = parseFloat(coordenadasJson[comuna][0]);
               let lng = parseFloat(coordenadasJson[comuna][1]);
               let marker = L.marker([lat, lng],{title:" Comuna "+comuna+" fotos: "+coordenadasJson[comuna][2]}).addTo(mymap);

               marker.on('click', function(comunaMarker) {


                   let lat = comunaMarker.latlng["lat"];
                   let lng = comunaMarker.latlng["lng"];
                   let comunaName;
                   for (let j = 0; j < coordenadas.length; j++) {
                       let coordinatesArray = coordenadas[j]
                       let latString = coordinatesArray[0];
                       let lngString = coordinatesArray[1];
                       let latFloat = parseFloat(latString);
                       let lngFloat = parseFloat(lngString);
                       if (lat === latFloat && lng === lngFloat) {
                           comunaName = comunas[j];
                           break;
                       }
                   }

                    let xhr2 = new XMLHttpRequest();
                    let data = new FormData();
                    data.append('comuna', comunaName);
                    xhr2.open('POST', 'listMap.py');
                    xhr2.send(data);
                    xhr2.timeout = 5000;
                    xhr2.onload = function (data) {
                        let listadoJson = JSON.parse(data.currentTarget.responseText);
                        let llaves = Object.keys(listadoJson);
                        let datos = Object.values(listadoJson);

                        html=`

                        <table>
                            <tr>
                                <th>Fecha Hora</th>
                                <th>Tipo</th>
                                <th>Estado</th>
                                <th>Foto</th>
                                <th>Enlace avistamiento</th>
                            </tr>`;

                        for (let i = 0; i< llaves.length; i++) {
                            let num = llaves[i]

                            let hr = listadoJson[num][0];
                            let tipo = listadoJson[num][1];
                            let estado = listadoJson[num][2];
                            let path = listadoJson[num][3];
                            let id = listadoJson[num][4];


                            html+= `<tr >
                                         <td>${hr}</td>
                                         <td>${tipo}</td>
                                         <td>${estado}</td>
                                         <td><img src=../media/${path} width="20" height="20" alt></td>
                                         <td><a href="infoCompleta.py?id=${id}">enlace</a></td>
                                     </tr>`;


                        }
                        html += `</table>`;


                        marker.bindPopup(html);
                    }
               });




        }


    }
    xhr.onerror = function () {
        alert('Ah ocurrido un error');
    }
</script>

  '''

print(map, file=utf8stdout)
