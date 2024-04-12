"""
Realizar la carga de dos números por teclado e imprimir la división del primero respecto al segundo, 
capturar la excepción ZeroDivisionError.
"""

#funcion de division de numeros
def division_numeros():
    #bucle infinito 
    while True:
        #intentamos
        try:
            #pedimos los numeros al user
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            #hacemos la division
            resultado = num1 / num2
            print("El resultado de la división es:", resultado)
        #eror si ingresa una division por 0
        except ZeroDivisionError:
            print("Error: No se puede dividir entre 0.")
        #error si ingresa una vaslor no numerico
        except ValueError:
            print("Error: Por favor, ingrese solo números.")
        else:
            break  #corta el programa

#llamamos a la funcion
division_numeros()
 