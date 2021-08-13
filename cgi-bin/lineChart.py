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
import datetime
import calendar

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


def findDay(date):
  born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
  return (calendar.day_name[born])


sql = "SELECT ALL dia_hora from detalle_avistamiento"
cursor.execute(sql)

dates = cursor.fetchall()

week_dict = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0,
             'Saturday': 0, 'Sunday': 0
             }

for d in dates:
  date = d[0].strftime('%d %m %Y')
  date_name = findDay(date)
  week_dict[date_name] += 1

json.dumps(week_dict)
print(json.dumps(week_dict))
