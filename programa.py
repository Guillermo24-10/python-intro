import funciones 

while True:
    try:
        menu  = int(input("""
    [1]Agregar Nueva pelicula
    [2]Obtener Peliculas
    [0]Salir                      
    >>>"""))
    
        if menu == 1:
            funciones.agregar_pelicula()
            print("Se Agrego la pelicula")
        elif menu == 2:
            funciones.obtener_peliculas()
        elif menu == 0:
            print("Saliendo del programa")
            exit()
    except ValueError as error:
      print(f"ingrese una opcion valida, {error}")
    