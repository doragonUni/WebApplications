#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
from database import Avistamientos

avistamientoDB = Avistamientos("localhost", "root", "", "tarea2")  # database del doctor

URL = cgi.FieldStorage()
id = cgi.FieldStorage().getfirst("id")

print("Content-type: text/html;charset=UTF-8\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

head = '''
<!DOCTYPE html>
<html lang="en">
<head>

  <title>Info</title>
  <link rel="title icon" href="../titleicon.png"/>

  <script src="../resize.js"></script>
  <style>

    body {
      background-color: rgb(238, 226, 208);
      font-family: "Helvetica";
      color: rgb(115, 54, 54);
    }

    .topBar {

      margin-left: 0;
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

    .complete-info{
      margin-top: 4%;
      margin-left: 20%;
    }
    .foto{
      margin-bottom: 5%;
    }
  </style>

</head>
<body>

<header>
  <div class="topBar">
    <nav>
      <a href="portada.py"><img alt="abeja para la pagina" src="../pageicon1.png"></a>
      <a href="../avistamientos.html">Informar un avistamiento</a>
      <a href="listaAvistamientos.py?page=0">Ver Listado</a>
      <a href="../Grafico.html">Ver Gráficos</a>
    </nav>

  </div>
</header>
'''
print(head, file=utf8stdout)

data = avistamientoDB.get_avistamiento(id)
comunaID = data[0][0]
regionID = avistamientoDB.get_regionID(comunaID)[0][0]
region = avistamientoDB.get_region(regionID)[0][0]
comuna = avistamientoDB.get_comunaNombre(comunaID)
fechaEnviada = data[0][1]
sector = data[0][2]
nombre = data[0][3]
mail = data[0][4]
telefono = data[0][5]
AVCount = avistamientoDB.count_avistamientos(id)[0][0]
FotoCount = avistamientoDB.count_foto(id)[0][0]
totalAvistamiento = AVCount

Personalinfo = f'''
<div class="complete-info">
  <div id="nombre">Nombre: {nombre} </div>
  <br>
  <div id="mail">Email: {mail} </div>
  <br>
  <div id="fono">Telefono: {telefono} </div>
  <br>
<div id="region">Region: {region}</div>
   <br>
<div id="comuna">Comuna: {comuna}</div>
   <br>
<div id="sector">Sector: {sector}</div>
   <br>
<div id="fechaEnviada">Fecha: {fechaEnviada}</div>
   <br>
<div id="totalAvitamientos">Total Avistamientos: {AVCount} </div>
    <br>
<div id="totalFoto">Total Fotos: {FotoCount} </div>
    <br>
    <br>
'''
print(Personalinfo, file=utf8stdout)
DaID = avistamientoDB.get_DAid(id)
i = 1;
for a in DaID:
  dID = a[0]
  tipo = avistamientoDB.get_tipo_estado(dID)[0][0]
  estado = avistamientoDB.get_tipo_estado(dID)[0][1]
  fechaInsecto = avistamientoDB.get_tipo_estado(dID)[0][2]
  allfotos = avistamientoDB.get_photo(dID)
  fotoCount = avistamientoDB.count_foto(dID)[0][0]
  insecto = f'''
  <div>Fecha Avistamiento insecto: {fechaInsecto} </div>
  <br>
  <div>Tipo: {tipo} </div>
     <br>
  <div>Estado: {estado}</div>
  '''
  print(insecto, file=utf8stdout)
  for f in allfotos:

    photo = f[0]

    row = f'''
              <div>
                <img class="foto" width="320" height="240"
                   id="foto{i}" alt="photo" src="../media/{str(photo)}" onclick="resize({i})" />
              </div>
      '''
    i += 1
    print(row, file=utf8stdout)
end = '''
</div>
  </body>
  </html>
  '''
print(end, file=utf8stdout)



