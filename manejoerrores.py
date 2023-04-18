
try:
    menu = int(input("Ingrese una opcion valida: "))
    print(f"ha ingresado la opcion {menu}")
except ValueError as error:
    print(f"no se puede ingresar ese tipo de dato, error: {error}")