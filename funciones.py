from modelos import *
import sql

def agregar_pelicula():
    
    nombre = str(input("Ingrese una pelicula para agregar: "))
    duracion = int(input("Ingrese una duracion para agregar: "))
    genero = str(input("Ingrese una genero para agregar: "))
    
    pelicula = Pelicula(nombre, duracion, genero)
    
    sql.agregar_pelicula(pelicula)
    
catalogo = Catalogo("PELICULAS DE ACCION")    
def obtener_peliculas():
    peliculas = sql.obtener_peliculas()
    for peli in peliculas:
         guarda_pelicula = Pelicula(peli[1],peli[2],peli[3])
         catalogo.peliculas.append(guarda_pelicula)
    
    for peli in catalogo.peliculas:
             print(f"""
Nombre de la Pelicula: {peli.nombre}                   
Duracion de la Pelicula: {peli.duracion} minutos                   
Genero de la Pelicula: {peli.genero}                    
""")