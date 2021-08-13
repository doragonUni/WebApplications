#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mysql.connector
import datetime
import hashlib
import os
import filetype



class Avistamientos:

  def __init__(self, host, user, password, database):
    self.db = mysql.connector.connect(
      host=host,
      user=user,
      password=password,
      database=database
    )
    self.cursor = self.db.cursor()

  # guarda los datos del user
  def save_avistamiento(self, data):
    sql = '''
    INSERT INTO avistamiento (comuna_id, dia_hora, sector, nombre, email, celular)
    VALUES (%s,%s,%s,%s,%s,%s)
    '''
    self.cursor.execute(sql, data)
    self.db.commit()
    return self.cursor.lastrowid

  def save_detalleAvistamiento(self, data, Aid):
    sql = '''
    INSERT INTO detalle_avistamiento (dia_hora, tipo, estado, avistamiento_id)
    VALUES (%s,%s,%s,%s)
    '''

    self.cursor.execute(sql, (*data[0:3], Aid))  # faltaid
    self.db.commit()
    return self.cursor.lastrowid

  def save_fotos(self, data, daID,path):
    filename = data.filename

    sql = '''
    INSERT INTO foto (ruta_archivo, nombre_archivo, detalle_avistamiento_id) VALUES (%s, %s, %s);
    '''
    self.cursor.execute(sql, (path, filename, daID))
    self.db.commit()

  def get_comuna(self, com):
    sql = f'''SELECT id FROM comuna WHERE nombre = "{com}"  '''
    self.cursor.execute(sql)
    return self.cursor.fetchall()[0][0]

  def get_comunaNombre(self, cid):
    sql = f'''SELECT nombre FROM comuna WHERE id = {cid}  '''
    self.cursor.execute(sql)
    return self.cursor.fetchall()[0][0]


  def get_last5(self):
    sql = '''
    SELECT DA.dia_hora, CO.nombre, AV.sector, DA.tipo, DA.id FROM avistamiento AV, detalle_avistamiento DA, comuna CO
    WHERE DA.avistamiento_id = AV.id AND AV.comuna_id=CO.id ORDER BY DA.dia_hora DESC LIMIT 5
    '''
    self.cursor.execute(sql)
    return self.cursor.fetchall()

  def get_tablaAvistamiento(self):
    sql = f'''
        SELECT DA.dia_hora, CO.nombre, AV.sector, AV.nombre, DA.id, AV.id FROM avistamiento AV, detalle_avistamiento DA, comuna CO
        WHERE DA.avistamiento_id = AV.id AND AV.comuna_id=CO.id ORDER BY DA.dia_hora DESC 5
        '''
    self.cursor.execute(sql)
    return self.cursor.fetchall()

  def get_tablaAvistamiento1(self):
    sql = f'''
            SELECT AV.id, CO.nombre, AV.dia_hora, AV.sector, AV.nombre FROM avistamiento AV, comuna CO
            WHERE AV.comuna_id=CO.id ORDER BY AV.dia_hora DESC
            '''
    self.cursor.execute(sql)
    return self.cursor.fetchall()

  def count_avistamientos(self, AVid):
    sql = f'''
    SELECT COUNT(*) FROM detalle_avistamiento WHERE avistamiento_id = {AVid}
    '''
    self.cursor.execute(sql)
    return self.cursor.fetchall()

  def count_foto(self, AVid):
    sql = f'''
    SELECT COUNT(*) FROM foto F, detalle_avistamiento DA WHERE F.detalle_avistamiento_id = DA.id and DA.avistamiento_id = {AVid}
        '''
    self.cursor.execute(sql)
    return self.cursor.fetchall()



  def get_photo(self, DAid):
    sql = f'''
        SELECT ruta_archivo from foto Where detalle_avistamiento_id = {DAid}
        '''
    self.cursor.execute(sql)
    return self.cursor.fetchall()


  def get_DAid(self, id):
    sql = f'''
    SELECT id from detalle_avistamiento Where avistamiento_id = {id}
    '''
    self.cursor.execute(sql)
    return self.cursor.fetchall()

  def get_tipo_estado(self, id):
    sql = f'''
        SELECT tipo, estado, dia_hora from detalle_avistamiento Where id = {id}
        '''
    self.cursor.execute(sql)
    return self.cursor.fetchall()


  def get_avistamiento(self, AVid):
    sql = f'''
    SELECT A.comuna_id, A.dia_hora, A.sector, A.nombre, A.email, A.celular FROM avistamiento A
     where id = {AVid}
    '''
    self.cursor.execute(sql)
    return self.cursor.fetchall()

  def get_regionID(self, cid):
    sql = f'''
        SELECT region_id FROM  comuna  where id = {cid}
        '''
    self.cursor.execute(sql)
    return self.cursor.fetchall()

  def get_region(self, rid):
    sql = f'''
            SELECT nombre FROM  region  where id = {rid}
            '''
    self.cursor.execute(sql)
    return self.cursor.fetchall()

  def get_countAllFotos(self):
    sql = "SELECT COUNT(id) FROM foto"
    self.cursor.execute(sql)
    total = self.cursor.fetchall()[0][0]
    return total

  def get_countFotosComuna(self):
    sql = ''' SELECT C.id, C.nombre, G.total
    FROM comuna as C,
    (SELECT A.comuna_id , COUNT(*) as total
    FROM detalle_avistamiento as D, foto as F, avistamiento as A
    WHERE A.id=D.avistamiento_id AND D.id = F.detalle_avistamiento_id
    GROUP BY A.comuna_id)
    as G WHERE C.id = G.comuna_id '''
    self.cursor.execute(sql)
    return self.cursor.fetchall()

  def get_listadoMapa(self, comuna):
    sql = f"""
          SELECT D.dia_hora, D.tipo, D.estado , F.ruta_archivo, A.id
          FROM detalle_avistamiento as D, foto as F, avistamiento as A,comuna as C
          WHERE D.id = F.detalle_avistamiento_id and D.avistamiento_id=A.id and A.comuna_id=C.id
          and C.nombre = "{comuna}"
      """
    self.cursor.execute(sql)
    return self.cursor.fetchall()




