"""
Escriba un programa que pregunte un año y que escriba si es bisiesto o no.
Se debe pasar por parámetro el año a una función.
Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los
múltiplos de 400 sí.
Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto,
1900 no es bisiesto.
"""

#funcion
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

#pedimos al user el año
anio = int(input("Ingrese un año: "))

# Verificar si es bisiesto utilizando la función
if es_bisiesto(anio):
    print(f"{anio} es bisiesto.")
else:
    print(f"{anio} no es bisiesto.")

