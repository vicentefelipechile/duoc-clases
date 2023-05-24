"""
La empresa dedicada a la venta de zapatos, ha decidido fabricar zapatos de
hombre para la venta online. Los zapatos tienen un
valor de $20.000 (cualquier número), pero podría variar según la demanda. 
Si la compra es igual o superior a $40.000 el envío es gratis,
en caso contario, debe cancelar un monto extra de $3.000 
Determine el total a pagar por una persona que requiere X cantidad de zapatos.
"""

precio: int = 20000
cantidad: int
while True:
    cantidad = int( input("Ingrese cantidad de zapatos: ") )

    if cantidad < 0:
        print("Error: Cantidad no valida de zapatos")
    else:
        break


print("====================")
print("=====  Boleta  =====")
print("====================")

print(f"Cantidad de zapatos: {cantidad}")
if cantidad * precio >= 40000:
    print(f"Costo de envio: 0")
else:
    print(f"Costo de envio: 3000")
print(f"Monto total: {cantidad * precio}")
