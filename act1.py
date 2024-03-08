"""
Generar un programa, que le permita al usuario buscar un valor dentro de una lista pre-construido y que nos
devuelva el lugar que ocupa.
Para ello se deberá utilizar una función que a partir de dos parámetros (la lista. y el elemento buscado) nos
devuelva el índice.
Por ejemplo, se busca el número 12 dentro del vector [8,12,9,45], la función devolverá el número 1, que es
el índice donde se encuentra el elemento buscado
"""

# Lista pre-construida
lista = [8, 12, 9, 45]

#funcion
def buscar_elemento(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return None

# Solicitar al user el numero a buscar
elemento_buscado = int(input("Ingrese el número a buscar: "))

# Llamar a la función
indice = buscar_elemento(lista, elemento_buscado)

# Verificar si se encontró el elemento
if indice is not None:
    print(f"El número {elemento_buscado} se encuentra en el índice {indice} de la lista.")
else:
    print(f"El número {elemento_buscado} no se encuentra en la lista.")



    
