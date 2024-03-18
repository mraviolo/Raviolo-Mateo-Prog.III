"""
Plantear una clase Operaciones que solicite en el método __init__ la carga de dos enteros e
inmediatamente muestre su suma, resta, multiplicación y división. Hacer cada operación en otro método de
la clase Operación y llamarlos desde el mismo método __init__
"""

#definimos la clase operaciones
class Operaciones:
    #iniciador
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.realizar_operaciones()

    #funcion para realizar las operaciones
    def realizar_operaciones(self):
        suma = self.sumar()
        resta = self.restar()
        multiplicacion = self.multiplicar()
        division = self.dividir()
        print("Suma:", suma)
        print("Resta:", resta)
        print("Multiplicación:", multiplicacion)
        print("División:", division)

    #funcion suma
    def sumar(self):
        return self.num1 + self.num2
    
    #funcion resta
    def restar(self):
        return self.num1 - self.num2
    
    #funcion multi
    def multiplicar(self):
        return self.num1 * self.num2
    
    #funcion dividir
    def dividir(self):
        #revisamos que la division no sea entre cero
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "No se puede dividir entre cero"

#le pedimos los atributos al user
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

#llamamos a la funcion
operaciones = Operaciones(num1, num2)
