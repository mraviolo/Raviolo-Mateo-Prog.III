"""
Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los
métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a
Definir dos objetos de la clase Alumno.
"""

#definimos la clase alumno
class Alumno:
    #iniciador
    def __init__(self, nombre, nota):
          self.nombre = nombre
          self.nota = nota
    
    #fucion que muestra el mensaje de la nota
    def quenotaes (nombre, nota):
        if nota >= 6:
             print(f"la nota {nota} de {nombre} es mayor")
        else:
             print(f"{nombre} no esta aprobado con la nota {nota}")

#le damos los atributos
alumno1 = Alumno("mateo", 9)

#llamamos a la funcion
alumno1.quenotaes()