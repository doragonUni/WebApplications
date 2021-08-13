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

sql = "SELECT ALL dia_hora from detalle_avistamiento where estado = 'muerto' "
cursor.execute(sql)

dead_month_dict = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0,
                   '06': 0, '07': 0, '08': 0, '09': 0, '10': 0,
                   '11': 0, '12': 0}

dead_date = cursor.fetchall()
for d in dead_date:
  # print(d[0])
  mes = d[0].strftime('%d/%m/%Y %H:%M:%S')
  dead_month_dict[mes[3:5]] += 1

sql = "SELECT ALL dia_hora from detalle_avistamiento where estado = 'vivo' "
cursor.execute(sql)

alive_month_dict = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0,
                    '06': 0, '07': 0, '08': 0, '09': 0, '10': 0,
                    '11': 0, '12': 0}
alive_date = cursor.fetchall()

for d in alive_date:
  # print(d[0])
  mes = d[0].strftime('%d/%m/%Y %H:%M:%S')
  alive_month_dict[mes[3:5]] += 1

sql = "SELECT ALL dia_hora from detalle_avistamiento where estado = 'no sé' "
cursor.execute(sql)

idk_month_dict = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0,
                  '06': 0, '07': 0, '08': 0, '09': 0, '10': 0,
                  '11': 0, '12': 0}
idk_date = cursor.fetchall()
for d in idk_date:
  mes = d[0].strftime('%d/%m/%Y %H:%M:%S')
  idk_month_dict[mes[3:5]] += 1

todo = {"dead": dead_month_dict, "alive": alive_month_dict, "idk": idk_month_dict}
json.dumps(todo)
print(json.dumps(todo))
