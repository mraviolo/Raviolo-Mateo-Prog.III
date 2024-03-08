"""
Realizar una función, que reciba como parámetro una lista compuesta por números enteros y que nos
devuelva otra lista con el mismo contenido pero ordenada de mayor a menor.
"""

#funcion
def ordenar_de_mayor_a_menor(lista):
    lista.sort(reverse=True)
    return lista

#lista orginal
numeros = [10, 3, 7, 1, 5]

#lista ordenada
lista_ordenada = ordenar_de_mayor_a_menor(numeros)

#imprimimos ambas
print("Lista original:", numeros)
print("Lista ordenada de mayor a menor:", lista_ordenada)
