"""
Se requiere implementar un sistema para el mesón de CineDuoc, en el cual,
va desde el sistema de venta de boletos, hasta los agregados (palomitas y bebidas).
Una simulación del sistema comienza con consultar al cliente si pertenece a
Duoc (estudiante o funcionario), el cliente muestra la placa o identificación
(en caso de tener) por lo que el vendedor registra en el sistema
True o False (Pertenece, no pertenece). Luego le consulta que entrada desea:

Las posibles entradas son:
⮚ Estreno → $4.800
⮚ Normal → $2.900

El cliente al seleccionar una, también debe indicar la cantidad que desea,
luego el sistema le consultará si desea agregar palomitas de maíz a su pedido,
si la respuesta es “si”, entonces el sistema muestra las siguientes promociones: 
⮚ Palomitas Pequeña → $2.500
⮚ Palomitas Mediana → $4.500
⮚ Palomitas Grande → $7.800


Una vez que ingresa el tipo, también debe seleccionar la cantidad.
Finalmente se le consulta si desea agregar bebidas al sistema de la misma forma: 
⮚ Bebida Pequeña → $1.000 
⮚ Bebida Mediana → $1.250 
⮚ Bebida Grande → $2.000

El sistema deberá mostrar el total a pagar por el cliente,
solicitar el efectivo e indicar el vuelto necesario para el cliente. 
Adicionalmente el sistema hará un descuento automático si el cliente
pertenece a Duoc, el descuento es de 30% y sólo se aplica a
las entradas compradas (no a las Palomitas ni Bebidas).
"""

esDuoc: bool = False
esValido: bool = False
esEstreno: bool = False
total: int = 0
totalEntradas: int = 0

print("")
print("============================================")
print("========== Bienvenido a Cine Duoc ==========")
print("============================================")
print("")

print("¿Usted tiene alguna promocion?")
print("1 ⮚ Persona normal")
print("2 ⮚ Estudiante Duoc")
print("3 ⮚ Funcionario Duoc")

while not esValido:
    tipoPromocion: int = int( input("Ingrese numero (1-3): ") )

    if tipoPromocion == 2 or tipoPromocion == 3:
        esDuoc = True
        esValido = True
    elif tipoPromocion == 1:
        esValido = True
    else:
        print("Error: El tipo de promocion no es valido")


print("")
print("Estan disponibles las siguientes entradas")
print("1 ⮚ Estreno → $4.800")
print("2 ⮚ Normal → $2.900")

esValido = False
while not esValido:
    tipoEntrada: int = int( input("Ingrese su entrada (1-2): ") )

    if tipoEntrada == 1:
        esEstreno = True
        esValido = True
        totalEntradas = 4800

    elif tipoEntrada == 2:
        esValido = True
        totalEntradas = 2900

    else:
        print("Error: El tipo de entrada no es valido")


print("")

esValido = False
while not esValido:
    promocion: str = input("¿Desea añadir palomitas de maiz? (s/n): ").lower()

    if promocion == "s":
        print("")
        print("Escoga el tipo de palomitas")
        print("1 ⮚ Palomitas Pequeña → $2.500")
        print("2 ⮚ Palomitas Mediana → $4.500")
        print("3 ⮚ Palomitas Grande → $7.800")

        palomitas: int = int( input("¿Que producto desea comprar?: ") )

        if palomitas == 1:
            total = total + 2500
        elif palomitas == 2:
            total = total + 4500
        elif palomitas == 3:
            total = total + 7800
        else:
            total = total

        esValido = True
    else:
        esValido = True


print("")

esValido = False
while not esValido:
    promocion: str = input("¿Desea añadir una bebida? (s/n): ").lower()

    if promocion == "s":
        print("")
        print("Escoga el tipo de bebida")
        print("1 ⮚ Bebida Pequeña → $1.000")
        print("2 ⮚ Bebida Mediana → $1.250")
        print("3 ⮚ Bebida Grande → $2.000")

        bebida: int = int( input("¿Que bebida desea comprar?: ") )

        if bebida == 1:
            total = total + 1000
        elif bebida == 2:
            total = total + 1250
        elif bebida == 3:
            total = total + 2000
        else:
            total = total

        esValido = True
    else:
        esValido = True



print("")
print("========== Boleta ==========")
print("")
print(f"Pelicula estreno: {esDuoc}")
print(f"Es funcionario de duoc: {esDuoc}")
if esDuoc:
    print(f"Promocion aplicada: -{totalEntradas * 0.3}")
    totalEntradas = totalEntradas * 0.7
print(f"Precio de entrada: {totalEntradas}")
print(f"Precio de bebidas y cabritas: {total}")
total = total + totalEntradas
print(f"Precio total: {total}")
print("")
print("========== Boleta ==========")

pagar: int = int( input("Ingrese monto a pagar: ") )
if pagar > total:
    print("Su vuelto es de:", pagar - total)
elif pagar == total:
    print("Gracias por su compra")
else:
    print("No tiene el suficiente dinero como para cubrir el gasto necesario de el total de esta boleta")
