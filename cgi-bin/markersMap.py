#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgitb
cgitb.enable()
from database import Avistamientos
import json

chileanCoords = None
with open("../chile.json") as file:
    chileanCoords = json.load(file)

print('Content-type: text/html; charset=UTF-8')
print('')

#avistamientoDB = Avistamientos("localhost", "root", "", "tarea2")
avistamientoDB = Avistamientos("localhost", "cc500246_u", "squeegetni", "cc500246_db")

def getComuna(name):
    for i in range(len(chileanCoords)):
        comuna = chileanCoords[i]
        nombre = comuna["name"]
        if (nombre == name):
            return comuna
    return ""

fotosComuna = avistamientoDB.get_countFotosComuna()

coordsDicc = {}
for fila in fotosComuna:
    comuna = getComuna(fila[1])
    coordsDicc[fila[1]] = [comuna['lat'], comuna['lng'], fila[2]]


print(json.dumps(coordsDicc))
