"""
Escribir una función que reciba como parámetro una palabra, y devuelva True si esa palabra es un
palíndromo y False si no lo es.
Ejemplo:
esCapicua("neuquen") === True
esCapicua("jovenes") === False
"""

#funcion
def esPalindromo(palabra):
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        print("true")
    else:
        print("false")

#pedimos al user la palabra
palabra_analizada = input("ingresa la palabra que quieres analizar: ")

#llamamos a la funcion
esPalindromo(palabra_analizada)