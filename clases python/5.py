"""
(HERENCIA) Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como
responsabilidades la carga por teclado y su impresión.
En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.
Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo
sueldo y muestre si debe pagar impuestos (sueldo superior a 3000)
También en el bloque principal del programa crear un objeto de la clase Empleado.
"""

#definimos la clase persona
class Persona:
    #iniciador
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #funcion para carga los datos del user
    def cargar_datos(self):
        self.nombre = input("Ingrese el nombre de la persona: ")
        self.edad = int(input("Ingrese la edad de la persona: "))

    #funcion para imprimir los datos
    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

#definimos la clase empleado que hereda de la clase padre (persona)
class Empleado(Persona):
    #iniciador
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    #fucion para pagar los impuestos
    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print(f"{self.nombre} debe pagar impuestos.")
        else:
            print(f"{self.nombre} no debe pagar impuestos.")

    #funcion para cargar los datos
    def cargar_datos(self):
        super().cargar_datos()
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))

    #funcion para imprimir los datos
    def imprimir_datos(self):
        super().imprimir_datos()
        print("Sueldo:", self.sueldo)


#aca creamos la persona
#le damos los atributos que nos dio el user y llamamos a las funcioes
print("Creación de la Persona:")
persona = Persona("", 0)  
persona.cargar_datos()     
persona.imprimir_datos()   

#aca creamos el empleado
#le damos los atributos que nos dio el user y llamamos a las funcioes
print("\n Creación de objeto Empleado:")
empleado = Empleado("", 0, 0.0)  
empleado.cargar_datos()          
empleado.imprimir_datos()        
empleado.pagar_impuestos()       
