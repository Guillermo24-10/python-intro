import sqlite3
from constantes import *

def conectar_db():
    conexion = sqlite3.connect(DATABASE_NAME)
    cursor = conexion.cursor()
    return conexion, cursor

def agregar_pelicula(pelicula):
    
    conexion, cursor = conectar_db()
    
    pelicula = (
        pelicula.nombre,
        pelicula.duracion,
        pelicula.genero
    )
    
    sql = f"INSERT INTO PELICULAS(NOMBRE,DURACION,GENERO) VALUES{pelicula}"
    cursor.execute(sql)
    
    conexion.commit()
    conexion.close()

def obtener_peliculas():
    
    conexion, cursor = conectar_db()
    sql = f"SELECT * FROM PELICULAS"
    cursor.execute(sql)
    peliculas = cursor.fetchall()
    conexion.commit()
    conexion.close() 
    return peliculas