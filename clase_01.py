caso = 3

# Script 1.0
if caso == 1:
    print("Hola!")
    nombre: str = input("Ingrese su nombre: ")

    print( f'Hola {nombre}' )



# Script 1.1
if caso == 2:
    print("Bienvenido al mundo de la programación")
    
    num1: int = int( input("Ingrese numero 1: ") )
    num2: int = int( input("Ingrese numero 2: ") )

    suma = num1 + num2
    print( f"La suma de los numeros es {suma}" )


# Script 1.2
if caso == 3:
    nombre: str = input("Ingrese su nombre: ")
    apelli: str = input("Ingrese su apellido: ")
    correo: str = input("Ingrese su correo: ")
    telefo: int = int( input("Ingrese su numero (+569): ") )
    rut: str = input("Ingrese su rut: ")

    print("Sus datos son: ")
    print( f"Nombre: {nombre} {apelli}" )
    print( f"RUT: {rut}" )
    print( f"Correo: {correo}" )
    print( f"Telefono: {telefo}")
