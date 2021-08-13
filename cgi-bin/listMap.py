#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgitb
import cgi
cgitb.enable()
import json

from database import Avistamientos

avistamientoDB = Avistamientos("localhost", "root", "", "tarea2")  # database del doctor
#avistamientoDB = Avistamientos("localhost", "cc500246_u", "squeegetni", "cc500246_db")

dicc = {}
print("Content-type: text/html\r\n\r\n")
utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)


nombreComuna = cgi.FieldStorage()
cantFotosPorComuna = avistamientoDB.get_listadoMapa(nombreComuna.getvalue('comuna'))

n = 0
for f in cantFotosPorComuna:
    dicc[n] = [f[0].strftime('%d/%m/%Y %H:%M'), f[1], f[2], f[3], f[4]]
    n = n + 1
print(json.dumps(dicc))

