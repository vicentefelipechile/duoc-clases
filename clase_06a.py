from os import system;system("cls")
# Al cerrar un expendio de naranjas, 15 clientes que aún no han pagado
# recibirán 15% de descuento si compran más de 10 Kgs.
# Determinar cuánto pagará cada cliente y cuánto percibirá
# la tienda por esas compras. El kilo de naranja cuesta $750.

clientes: int = 15
descuento: int = 15

for i in range(clientes):
    i+=1

    print("")
    print(f"Cliente {i}")

    peso = input("Ingrese el peso de sus naranjas: ")
    precio: float = 750

    if peso == "":
        break

    peso: float = float(peso)

    if peso >= 10:
        precio /= 1 + descuento / 100
        precio = round(precio, 2)

    total = round( peso * precio, 1 )
    
    print(f"Usted debe pagar {total} por los {peso}kg de naranja")