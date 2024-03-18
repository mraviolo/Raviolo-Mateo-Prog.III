"""
Declarar una clase llamada Familia. Definir como atributos el nombre del padre, madre y una lista con los
nombres de los hijos.
Definir el método especial __str__ que retorne un string con el nombre del padre, la madre y de todos sus
hijos
"""

#definimos la clase familia
class Familia:
    #iniciador
    def __init__(self, nombre_padre, nombre_madre, hijos=[]):
        self.nombre_padre = nombre_padre
        self.nombre_madre = nombre_madre
        self.hijos = hijos

    #funcion str para imprimit el mensaje 
    def __str__(self):
        hijos_str = ", ".join(self.hijos)
        return f"Padre: {self.nombre_padre}, Madre: {self.nombre_madre}, Hijos: {hijos_str}"

#le damos atributos a la familia
familia1 = Familia("Jorge", "Anna", ["Mateo", "Lucas", "Leo"])

#imprimimos la familia
print(familia1)
