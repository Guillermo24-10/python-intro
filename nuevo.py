#FUNCION 1
"""def f(x,y,z):
 x=x+1
 y.append(23)
 print(x,y,z)
 
x=22
y=[22]
z=24
f(x,y,z)
print(x,y,z) """

#FUNCION 2
"""def f(x,y):
    return x*2,y*2

a,b=f(1,2)
print(a,b)"""

#FUNCION 4
"""class Terrestre:
    def desplazar(self):
        print("el animal anda")
class Acuatico:
    def desplazar(self):
        print("el animal nada")    

class Cocodrillo(Acuatico,Terrestre):
    pass

c=Cocodrillo()
c.desplazar()"""

#EJERCICIO 1
"""Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24."""


"""def sumar(lista): 
        suma=0
        for i in range(0,len(lista)):
            suma+=lista[i]
        return suma

def multiplicar(lista):
        multiplicar=1
        for i in range(0,len(lista)):
            multiplicar*=lista[i]
        return multiplicar
        
x=sumar([1,2,3,4])
print(x)

y=multiplicar([1,2,3,4])
print(y)"""

#EJERCICIO 2
""""Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False."""                
"""def x(a):
    lista=['a','e','i','o','u']
    for i in range(0,len(lista)):
        if a==lista[i]:
            return True
        else:
            return False    

t=x('a')
print(t)
            """
            
#EJERCICIO 3                
"""Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga."""

"""def mas_larga(cadena):
    lista=[]
    for i in range(0,len(cadena)):
            z = cadena[i]
            lista.append(len(z))
            y = max(lista)    
    for j in range(0,len(cadena)):
        if y==len(cadena[j]):
         return cadena[j]
                           
x=mas_larga(['maria','juan','guillermo','jose','santiago'])
print(x)     """              

#EJERCICIO 4

      