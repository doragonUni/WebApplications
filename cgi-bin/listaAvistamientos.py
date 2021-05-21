#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
from datetime import datetime
import sys
import os
from io import TextIOWrapper
from database import Avistamientos

import filetype

avistamientoDB = Avistamientos("localhost", "cc500246_u", "squeegetni", "cc500246_db") # database del doctor  # tenemos la data

print("Content-type: text/html;charset=UTF-8\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)


page = cgi.FieldStorage().getfirst("page")
page = int(page)


head = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Listado</title>
  <link rel="title icon" href="../titleicon.png"/>
  <script src="../redirect.js"></script>



  <style>

    body {
      background-color: rgb(238, 226, 208);
      font-family: "Helvetica";
      color: rgb(115, 54, 54);
    }

    .listado-avistamientos {
      margin-top: 5%;
    }

    .topBar {

      margin-left: 0%;
      overflow: hidden;
      background-color: rgb(91, 124, 91);

    }

    .topBar img {
      display: inline-block;
      object-fit: scale-down;

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

    table, th, td {
      border: 1px solid black;
      border-collapse: collapse;
      text-align: left;
      padding: 10px;
      margin-bottom: 10%;

    }

    .table {
      width: 70%;
      margin-left: auto;
      margin-right: auto;
      color: black;

    }

    .table-title {
      margin-left: 40%;
    }

    .pageDiv{
      margin-left: 70%
    }


  </style>

</head>
'''

print(head, file=utf8stdout)

header = '''
<body>

<header>
  <div class="topBar">
    <nav>
      <a href="portada.py"><img alt="icono pagina abeja" src="../pageicon1.png"></a>
      <a href="../avistamientos.html">Informar un avistamiento</a>
      <a href="../Grafico.html">Ver Graficos</a>
    </nav>

  </div>
</header>
'''
print(header, file=utf8stdout)

topBody = '''<div class="listado-avistamientos ">
  <h2 class="table-title">Listado de avistamientos</h2>
  <table class="table" id="listaAvistamientos">
    <thead >
    <tr>
      <th>Fecha-Hora</th>
      <th>Comuna</th>
      <th>Sector</th>
      <th>Nombre contacto</th>
      <th>Total avistamientos</th>
      <th>Total Fotos</th>
    </tr>
    </thead>'''

print(topBody, file=utf8stdout)


data1 = avistamientoDB.get_tablaAvistamiento1()
data1 = data1[int(page)*5:int(page)*5+5]
totalDACount = 0
for d in data1:
  id = d[0]
  AVCount = avistamientoDB.count_avistamientos(id)[0][0]
  DAID = avistamientoDB.get_DAid(id)[0][0]
  DACount = avistamientoDB.count_foto(id)[0][0]




  row = f'''
            <tr onclick="redirect({id})">
                <th>{str(d[2])}</th>
                <th>{str(d[1])}</th>
                <th>{str(d[3])}</th>
                <th>{str(d[4])}</th>
                <th>{str(AVCount)}</th>
                <th>{str(DACount)}</th>

    '''
  print(row, file=utf8stdout)


bottomTable = '''
    </tbody>
  </table>
</div>
'''

page += 1

prev = page - 2
if prev < 0:
  prev = 0

print(bottomTable, file=utf8stdout)
end = f'''

  <div class="pageDiv">
  <a href="listaAvistamientos.py?page={prev}">PREV</a>
  <a href="listaAvistamientos.py?page={page}">NEXT</a>
  </div>

</body>
</html>
'''
print(end, file=utf8stdout)
