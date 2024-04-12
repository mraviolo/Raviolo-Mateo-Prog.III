"""
Realizar la carga de dos números por teclado e imprimir la división del primero respecto al segundo, 
capturar las excepciones ZeroDivisionError y ValueError.
"""

#funcion de la division
def division():
    #intentamos
    try:
        #pedimos los numeros al user
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        #los dividimos
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    #eerror al dividir entre cero
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero. Intente de nuevo.")
    #error si el valor es incorrecto, no numerico
    except ValueError:
        print("Error: Ingrese un número válido. Intente de nuevo.")

#llamamos a la funcion
division()
