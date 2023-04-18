
def leer_fichero():
    file = open('file.txt', 'r') # 'r' > modo lectura
    dato = file.read()
    file.close()
    print(dato)

leer_fichero()

def escribir_fichero():
    file = open('file.txt', 'w') # 'w' > modo escritura
    dato = 'Mi apellido es Paredes'
    file.write(dato)
    file.close()
#leer_fichero()

file = open('file.txt', 'a') # 'a' > modo agregar escritura
dato = '\nEsta linea es nueva escritura'
file.writelines(dato)
file.close()
leer_fichero()

