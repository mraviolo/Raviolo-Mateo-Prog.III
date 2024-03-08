"""
Cuando en un número la diferencia entre cada par de dígitos consecutivos es uno, se lo llama número "step"
(como el 123234, el 9876787654, etc.).
Escribir una función, que reciba como parámetro un número y devuelva True si es un número step o False si
no lo es.
"""

#funcion
def es_numero_step(numero):
    numero_str = str(numero)
    for i in range(len(numero_str) - 1):
        digito_actual = int(numero_str[i])
        digito_siguiente = int(numero_str[i + 1])
        if abs(digito_actual - digito_siguiente) != 1:
            print("no es numero step")
    print("es numero step")

#pedimos al user un numero
num = int(input("introduce un numero a analizar: "))

#llamamos a la funcion
es_numero_step(num)
