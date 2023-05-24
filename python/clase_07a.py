from os import system;system("cls")
# Crear un menu
# Declar una variabla llamada validar para controlar el ciclo whiel

validar: bool = True
X: int = None
Y: int = None

while validar:

    # Presentar las opciones
    print("")
    print(" = =========================== =")
    print(" = Porfavor ingrese una opcion =")
    print(" = 1 -> Sumar                  =")
    print(" = 2 -> Restar                 =")
    print(" = 3 -> Salir                  =")
    print(" = =========================== =")

    opcion: str
    try:
        opcion = input("Opcion: ")
    except KeyboardInterrupt:
        opcion = "3"
    except EOFError:
        opcion = "3"

    print("")

    if opcion == "1":
        print("Sumando...")
        print(" = =========================== =")

        try:
            X = int( input("Ingrese valor de X: ") )
        except ValueError:
            print("= Error: El numero no es valido, estableciendolo a 1")
            X = 1

        try:
            Y = int( input("Ingrese valor de Y: ") )
        except ValueError:
            print("= Error: El numero no es valido, estableciendolo a 1")
            Y = 1

        print(f"= El resultado es: {X+Y}")
        print(" = =========================== =")

    elif opcion == "2":
        print("Restando...")
    elif opcion == "3":
        print("Saliendo...")
        validar = False
    else:
        print("Ingrese una opcion valida pe")
