"""
Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre y dos
métodos (funciones), uno de dichos métodos inicializará el atributo nombre y el siguiente método mostrará
en la pantalla el contenido del mismo.
Definir dos objetos de la clase Persona
"""

#definimos la clase persona
class Persona:
    #iniciador
    def __init__(self, nombre):
        self.nombre = nombre
    
    #funcion para imprimir el nombre
    def mostrar_nombre(self):
        print("Nombre:", self.nombre)

#le damos los atributos
persona1 = Persona("Juan")
persona2 = Persona("Maria")

#llamamos a la funcion
persona1.mostrar_nombre()
persona2.mostrar_nombre()
