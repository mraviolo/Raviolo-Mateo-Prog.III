"""
Escribir una función que reciba como parámetro una frase y devuelva la cantidad de vocales que ésta tiene.
"""
#creamos un contador aux
contador = 0

#lista de vocales
vocales = ["a","e","i","o","u"]

#funcion
def cuenta_vocales(texto, contador):
    for i in texto:
        if i in vocales:
            contador += 1
        else:
            pass
    print(f"la cantidad de vocales en el texto es de: {contador}")

#pedimos al user el texto
texto1 = input("intrudoce el texto a analizar: ").lower()

#llamamos a la funcion
cuenta_vocales(texto1, contador)