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


print("Content-type: text/html;charset=UTF-8\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)


avistamientoDB = Avistamientos("localhost", "cc500246_u", "squeegetni", "cc500246_db")  # database del doctor
data = avistamientoDB.get_last5()  # tenemos la data


head = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Portada</title>

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
  photo = avistamientoDB.get_photo(d[4])[0][0] #primer 0 determina la ultima foto, 1 pa la siguiente y asi...
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

footer = '''
</tbody>
</table>
</div>
'''
print(footer, file=utf8stdout)



