#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
from datetime import datetime
import sys
import os
from io import TextIOWrapper
from html import escape
import re as regex
import filetype
import hashlib

from database import Avistamientos

cgitb.enable()

print("Content-type: text/html;charset=UTF-8\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

form = cgi.FieldStorage()  # Guardamos la info del cliente
avistamientoDB = Avistamientos("localhost", "cc500246_u", "squeegetni", "cc500246_db") # Base de datos para los avistamientos
MAX_FILE_SIZE = 1000000
error = ""


def deleteFiles(lista):
  for l in lista:
    for e in l:
      os.remove('../media/' + e)


head = '''<!DOCTYPE html>
<html lang="en">
<head>
  <title>Felicidades</title>
  <link rel="title icon" href="../titleicon.png"/>

  <style>


    body {
      background-color: rgb(238, 226, 208);
      font-family: "Helvetica";
      color: rgb(115, 54, 54);
    }

    h1{
      text-align: center;
    }

    .gracias{
      margin-left: 33%;
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
  </style>
</head>
'''
print(head, file=utf8stdout)

hashlist = []

if len(form) > 0:
  insectCV = 1
  fotoCV = 0
  # print("LARGO INSECTOS:", len(form.getlist("estado-avistamiento")))
  n = avistamientoDB.get_countAllFotos()


  for i in range(len(form.getlist("estado-avistamiento"))):
    dia = form.getlist("dia-hora-avistamiento")[i]
    if type(dia) != str or len(dia) == "":
      error += "fecha incorrecta\n"
    tipo = form.getlist("tipo-avistamiento")[i]
    if type(tipo) != str or len(tipo) == "":
      error += "tipo incorrecto\n"
    estado = form.getlist("estado-avistamiento")[i]
    if type(estado) != str or len(estado) == "":
      error += "tipo incorrecto\n"
    hash = []


    while f'foto-avistamiento{insectCV}{fotoCV}' in form.keys():

      # print(f'foto-avistamiento{insectCV}{fotoCV}')
      # print(insectCV, fotoCV)
      img = form[f'foto-avistamiento{insectCV}{fotoCV}']
      if img.filename:
        try:
          size = os.fstat(img.file.fileno()).st_size
          imgname = img.filename
          # print("tamano imagen", size)
          if size > MAX_FILE_SIZE:
            error += f'''foto:{imgname} excede tamaño max (1MB).\n'''
            # guardar el archivo

          total=n+1
          n=n+1
          hash_file = str(total) + hashlib.sha256(imgname.encode()).hexdigest()[0:30]
          file_path = '../media/' + hash_file
          open(file_path, 'wb').write(img.file.read())
          tipo = filetype.guess(file_path)

          hash.append(hash_file)
          if (tipo.mime != 'image/jpg') and (tipo.mime != 'image/png') and (tipo.mime != 'image/jpeg'):
            hashlist.append(hash)
            deleteFiles(hashlist)
            error += '''foto no es de formato .png, .jpg, .jpeg'''
        except IOError as e:
          error += "error en la foto"

      fotoCV += 1
    hashlist.append(hash)
    insectCV += 1
    fotoCV = 0

  phoneRegex = "^[2-9]([0-9]{8})*$"
  mailRegex = "[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
  region = escape(form['region'].value)
  sector = escape(form['sector'].value)
  if len(sector) > 100:
    error += "largo de sector excedido.\n"
  nombre = escape(form['nombre'].value)
  if type(nombre) != str or (len(nombre) == 0 or len(nombre) > 200):
    error += "nombre incorrecto. \n"
  email = escape(form['email'].value)
  if type(email) != str or not (regex.search(mailRegex, email)):
    error += "mail incorrecto.\n"
  celular = escape(form['celular'].value)
  if len(celular) > 0 and not (regex.search(phoneRegex, celular)):
    error += "celular incorrecto.\n"
  # print(error)
  if error != "":
    body = f'''
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

        <h1>{error}</h1>
        </body>
        </html>
        '''
    print(body, file=utf8stdout)

  else:
    #print(hashlist)

    comunaForm = escape(form['comuna'].value)  # dado el nombre de la comuna, la pasamos al id
    comunaID = avistamientoDB.get_comuna(comunaForm)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    personalData = (
    comunaID, time, escape(form['sector'].value), escape(form['nombre'].value), escape(form['email'].value),
    escape(form['celular'].value))

    personalID = avistamientoDB.save_avistamiento(personalData)
    fotoC = 0
    insectC = 1
    for i in range(len(form.getlist("estado-avistamiento"))):
      dia = escape(form.getlist("dia-hora-avistamiento")[i])
      tipo = escape(form.getlist("tipo-avistamiento")[i])
      estado = escape(form.getlist("estado-avistamiento")[i])
      dataAvist = (dia, tipo, estado, personalID)
      detalleID = avistamientoDB.save_detalleAvistamiento(dataAvist, personalID)

      while f'foto-avistamiento{insectC}{fotoC}' in form.keys():
        img = form[f'foto-avistamiento{insectC}{fotoC}']
        #print(hashlist[insectC-1][fotoC])
        #print(insectC, fotoC)
        if img.filename:
          avistamientoDB.save_fotos(img, detalleID,hashlist[insectC-1][fotoC])
        fotoC += 1
      insectC += 1
      fotoC = 0
    body1 = '''
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

    <h1>Hemos recibido su información, muchas gracias por colaborar</h1>
    <div class="gracias"><img alt="gracias foto meme" src="../grasias.jpg"></div>

    </body>
    </html>
    '''

    print(body1, file=utf8stdout)
