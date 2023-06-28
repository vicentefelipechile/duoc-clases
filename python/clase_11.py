#---------------------
#----- VARIABLES -----
#---------------------

# Valores por defecto
ALUMNOS: list = []
VALIDAR: bool = True

#---------------------
#----- FUNCIONES -----
#---------------------

# Verificador simple de ruts
def VerificarRut(rut: str = None, retornar: bool = False) -> str | None:
    if not rut:
        return False
    
    rut = rut.replace(".", "")
    datos: list[str] = rut.split("-")
    
    if not ( len( datos ) == 2 ):
        return False
    
    if not ( datos[0].isnumeric() ):
        return False
    
    if not ( len( datos[0] ) == 8 ):
        return False
    
    if not ( datos[1].isnumeric() or datos[1].lower() == "k" ):
        return False
    
    if retornar:
        return f"{datos[0]}-{datos[1]}"
        
    return True



# Insertar alumnos
def InsertarAlumno(rut: str = None, nombre: str = None, apellido: str = None, fecha: str = None, carrera: str = None, asignaturas: dict = None) -> bool:
    if not VerificarRut(rut):
        return False
    
    #if not ( nombre and apellido and fecha and carrera and asignaturas ):
    #    return False
    
    #if not ( isinstance(asignaturas, dict) ):
    #    return False
    
    rut = VerificarRut(rut, retornar=True)
    
    ALUMNOS.append({
        "Rut": rut,
        "Nombre": nombre,
        "Apellido": apellido,
        "Fecha": fecha,
        "Carrera": carrera,
        "Asignaturas": asignaturas
    })
    
    return True

# InsertarAlumno("21.126.938-0", "Vicente", "Cortes", "04-12-2002", "Ingeniera en Informatica", {"El pepe":"Etesech"})
def InsertarDatos(nombre: str = "Dato") -> str:
    
    # Algoritmo bien loco para saber si es femenino la palabra
    prefijo: str = "La" if nombre.split(" ")[0][-1:].lower() == "a" else "El"
    
    while True:
        try:
            dato: str = input(f"Introduzca {prefijo.lower()} {nombre}: ")
            if dato == "":
                raise Exception
        except Exception:
            print(f"Error: {prefijo} {nombre} colocado no es valido")
        else:
            break
    
    return dato
    


# Funciones principales
def Grabar():
    print("======================================")
    print("============ Grabar Datos ============")
    print("======================================")

    # Validar Rut
    while True:
        try:
            Rut: str = input("Introduzca RUT: ")
            if not VerificarRut(Rut):
                raise Exception
        except Exception:
            print("Error: El RUT colocado no es valido")
        else:
            break

    # Validar Nombre
    while True:
        try:
            Nombre: str = input(f"Introduzca el Nombre: ")
            if Nombre == "":
                raise Exception

            if not ( len(Nombre) >= 2 and len(Nombre) <= 12):
                raise Exception

        except Exception:
            print(f"Error: el Nombre colocado no es valido")
        else:
            break

    # Validar Apellido
    Apellido = InsertarDatos("Apellido")

    # Validar Fecha de Nacimiento
    print("Formato fecha: (DD-MM-AAAA) ej: 26-04-1998")
    Fecha = InsertarDatos("Fecha de nacimiento")

    # Validar Carrera
    Carrera = InsertarDatos("Carrera")
    
    # Añadir asignaturas
    Asignaturas: list = []
    i: int = 1
    
    while True:
        print("== Para salir solo escriba \"Salir\" ==")
        try:
            asignatura = input(f"[{i}] Introduzca asignatura: ")
            if asignatura == "":
                raise Exception
            
            if asignatura.lower() == "salir":
                raise NameError

            try:
                promedio = float( input(f"[{i}] Introduzca promedio de {asignatura}: ") )
                if not ( promedio >= 1 and promedio <= 7):
                    raise ZeroDivisionError

            except ValueError:
                raise ZeroDivisionError
        
        except NameError:
            break
        except ZeroDivisionError:
            print(f"Error: [{i}] El promedio colocado no es valido")
        except Exception:
            print(f"Error: [{i}] El nombre de la asignatura no es valido")
        else:
            Asignaturas.append((asignatura, promedio))
            i += 1

    InsertarAlumno(Rut, Nombre, Apellido, Fecha, Carrera, Asignaturas)


def Buscar():
    print("======================================")
    print("============ Buscar Datos ============")
    print("======================================")
    
    while True:
        rut = input("Introduzca el rut a buscar: ")

        if not VerificarRut(rut):
            print("Error: El rut ingresado no es valido")
            continue
        
        rut = VerificarRut(rut, retornar=True)

        for i in range( len(ALUMNOS) ):
            if ALUMNOS[i]["Rut"] == rut:
                Datos = dict( ALUMNOS[i] )
                Nombre = Datos.get("Nombre")
                Apellido = Datos.get("Apellido")
                Fecha = Datos.get("Fecha")
                Carrera = Datos.get("Carrera")
                Asignaturas = Datos.get("Asignaturas")

                print(f" === Alumno {Nombre} encontrado! ===")
                print(f"Nombre: {Nombre}")
                print(f"Apellido: {Apellido}")
                print(f"Fecha de nacimiento: {Fecha}")
                print(f"Carrera: {Carrera}")
                for y in range( len(Asignaturas) ):
                    y += 1
                    print(f"[{y}] Asignatura: {Asignaturas[y][0]}")
                    print(f"[{y}] Promedio: {Asignaturas[y][1]}")


def main():

    while True:
        print("======================================")
        print("============ Certificados ============")
        print("======================================")
        
        print("Ingrese su opcion: ")
        print("[1] Ingresar Datos ")
        print("[2] Buscar Datos ")
        print("[3] Imprimir Datos (No funciona) ")
        print("[4] Salir ")

        try:
            opcion = int( input("Opcion: ") )
            if not ( opcion >= 1 and opcion <= 4 ):
                raise Exception
        except ValueError:
            print("Error: Datos no validos")
        except Exception:
            print("Error: Opcion no valida")
        else:
            if opcion == 1:
                Grabar()
            elif opcion == 2:
                Buscar()
            elif opcion == 4:
                print("Tenga un buen dia!")
                exit()

main()
