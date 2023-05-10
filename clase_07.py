from os import system;system("cls")
# Uso de Raise
# Uso de Finally
# Excepcion de OverFlowError
# Excepcion de ValueError

numero: int = None

try:
    numero = int( input("Ingrese un numero: ") )
except ValueError:
    print("Pero... el numero que colocaste no se pudo convertir, colocaste un numero o no?")

finally:
    if type(numero) is int:
        print("Colocaste un numero entero")
    else:
        print("No colocaste un numero entero")

