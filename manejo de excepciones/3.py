"""
Almacenar en una tupla los nombres de meses del año. Solicitar el ingreso del número de mes y mostrar 
seguidamente el nombre de dicho mes. Capturar la excepción IndexError.
"""

#funcion de los meses
def num_meses():
    #tupla de meses
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    #intentamos
    try:
        #Solicitar el mes al usuario
        numero_mes = int(input("Ingresa el número de mes (1-12): "))
        #verificamos si existe
        if numero_mes < 1 or numero_mes > 12:
            raise ValueError("Número de mes fuera de rango")
        #le restamos uno ya que la tupla arranca desde el numero 0
        nombre_mes = meses[numero_mes - 1]
        print(f"El mes correspondiente al número {numero_mes} es: {nombre_mes}")
    #error al ingresas un vlaor incorrecto 
    except ValueError:
        print("Error: Ingresa un número válido.")
    #error si el numero de mes esta fuera de ranfgo
    except IndexError:
        print("Error: Número de mes fuera de rango.")
    
#llamamos a la fucnion
num_meses()
