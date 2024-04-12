"""
Realizar la carga de dos números enteros por teclado e imprimir su suma, luego preguntar si quiere 
seguir sumando valores. Codificar un programas uno que capture la excepción de ingreso de datos no 
numérico.
"""

#funcion de suma de numeros
def suma_numeros():
    #bucle infinito
    while True:
        #intentamos
        try:
            #pedimos los numeros al user
            num1 = int(input("Ingrese el primer número entero: "))
            num2 = int(input("Ingrese el segundo número entero: "))
            #los sumamos
            suma = num1 + num2
            print("La suma de los números es:", suma)
        #error si ingresa numeros no enteros
        except ValueError:
            print("Error: Por favor, ingrese solo números enteros.")
        #opcion para salir del programa
        finally:
            seguir = input("¿Quiere seguir sumando valores? (s/n): ")
            if seguir.lower() != 's':
                break
#llamamos a la funcion
suma_numeros()
