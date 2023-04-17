#import os;print(os.getcwd())
caso = 4


# Script 2.0
if caso == 1:

    num1 = int( input("Ingrese numero 1: ") )
    num2 = int( input("Ingrese numero 2: ") )

    if num1 > num2:
        print(f"El numero 1 ({num1}) es mayor que el numero 2 ({num2})")
    elif num2 > num1:
        print(f"El numero 2 ({num2}) es mayor que el numero 1 ({num1})")
    else:
        print("Ambos numeros son iguales")



# Script 2.1
if caso == 2:
    num1 = int( input("Ingrese numero 1: ") )
    num2 = int( input("Ingrese numero 2: ") )

    if num1 > 0:
        if num2 > 0:
            print(f"La suma de los numeros da en total {num1 + num2}")
        else:
            print(f"Error: El numero 2 ({num2}) no es positivo")
    else:
        print(f"Error: El numero 1 ({num1}) no es positivo")



# Script 2.2
if caso == 3:
    num = int( input("Ingrese su numero: ") )

    if num > 0:
        for x in range(1, 11):
            print(f" {num} x {x} = {num * x}")
    else:
        print(f"Error: El numero ({num}) no es valido")



# Script 2.3
if caso == 4:
    num = int( input("Ingrese numero (1 a 101): ") )

    #Python avanzado
    print( f"Error: El numero ({num}) no es valido" if not ( num >= 1 and num <= 101 ) else "El numero es impar" if num % 2 == 1 else "El numero es par" )

    if num >= 1 and num <= 101:
        if num % 2 == 1:
            print("El numero es impar")
        else:
            print("El numero es par")
    else:
        print(f"Error: El numero ({num}) no es valido")