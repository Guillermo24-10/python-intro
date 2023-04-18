"""class Arma:
    def __init__(self,balas,peso):
        self.balas=balas
        self.peso=peso
    def disparar(self):
        print("El arma está disparando")
        
class Pistola(Arma):
    
    def disparar(self):
        return super().disparar()
    

arma = Arma(15,8)
arma.disparar()
pistola = Pistola(12,9)
pistola.disparar()           """

class Curso:
    __titulo = "Curso de Python"
    __duracion = 10
    
    def __adquirir_curso(self):
        print("Has adquirido el curso") #__ => los guiones significa privados                    
    
    def get_adquirir_curso(self):
        return self.__adquirir_curso()    
    
    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self,titulo):
        self.__titulo = titulo
        print(self.__titulo)
    
curso = Curso()
curso.get_adquirir_curso()
curso.get_titulo()    
curso.set_titulo("Curso de C++")
        