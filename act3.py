"""
Escriba un programa que pida ancho y alto de un rectángulo y el caracter a utilizar en el dibujo.
Ejemplo:
Pedido:
Ancho: 5
Alto: 4
Caracter: 'A'
Imprime:
A A A A A
A A A A A
A A A A A
A A A A A
"""

#fucion
def grafico(ancho, alto, caracter):
    for i in range(alto):
        for j in range(ancho):
            print(caracter, end=" ")
        print()

#pedimos al user los datos para el grafico
ancho = int(input("Ingrese el ancho del rectángulo: "))
alto = int(input("Ingrese el alto del rectángulo: "))
caracter = input("Ingrese el carácter para dibujar el rectángulo: ")

#llamamos a la funcion
print("Rectángulo dibujado:")
grafico(ancho, alto, caracter)
