#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
from datetime import datetime
import sys
import os
from io import TextIOWrapper
import json
import mysql.connector

connector = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="tarea2"
 )

#connector = mysql.connector.connect(
 # host="localhost",
  #user="cc500246_u",
  #password="squeegetni",
  #database="cc500246_db"
#)


cursor = connector.cursor()
print('Content-type: text/html; charset=UTF-8')
print('')

sql = "SELECT Count(*) from detalle_avistamiento where tipo = 'arácnido' "
cursor.execute(sql)

spiders = cursor.fetchall()[0][0]

sql = "SELECT Count(*) from detalle_avistamiento where tipo = 'insecto' "
cursor.execute(sql)

insects = cursor.fetchall()[0][0]

sql = "SELECT Count(*) from detalle_avistamiento where tipo = 'miriápodo' "
cursor.execute(sql)

mirapods = cursor.fetchall()[0][0]

sql = "SELECT Count(*) from detalle_avistamiento where tipo = 'no sé' "
cursor.execute(sql)

idk = cursor.fetchall()[0][0]

quantity = {'aracnidos': spiders, 'miriapodo': mirapods, 'insecto': insects, 'nose': idk
            }


json.dumps(quantity)
print(json.dumps(quantity))

cursor.close()

