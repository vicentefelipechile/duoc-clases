# Ingresar por teclado 5 numeros enteros, luego debe indicar:
# - Cuantos numeros son mayores a cero
# - Cuantos numeros son menores a cero
# - Cuantos numeros son iguales a cero

from os import system;system("cls")


numeros: list = []

for i in range(5):
    i = i + 1

    numero = int( input(f"Ingrese numero {i}: ") )
    numeros.append(numero)

for k in numeros:
    
    if k > 0:
        print(f"El numero {k} es mayor que 0")
    elif k == 0:
        print(f"El numero {k} es cero")
    else:
        print(f"El numero {k} es menor que 0")
