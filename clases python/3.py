"""
Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos:
inicializar los atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. El
nombre de la clase llamarla Triangulo.
"""

#definimos la clase triangulo
class Triangulo:
    #iniciador
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    #funcion para saber que lado es mayot
    def imprimir_lado_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print("El lado mayor es:", mayor)
    
    #funcion para saber si es equilatero
    def es_equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero")
        else:
            print("El triángulo no es equilátero")

#le pedimos al user que ingrese los lados del triángulo
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

#le damos los atributos asignados por el user
triangulo = Triangulo(lado1, lado2, lado3)

#llamamos a la funcion
triangulo.imprimir_lado_mayor()
triangulo.es_equilatero()
