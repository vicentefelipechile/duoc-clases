# ============================
# ===== IMPORTAR MODULOS =====
# ============================

import numpy as np


# ============================
# ===== DEFINIR VARIABLES ====
# ============================

# Para que ordenar el array si se puede mostrarlo ordenado
# cuando el usuario pida ver los asientos.
UBICACIONES = np.array( np.arange(1, 101), dtype=str )
UBICACIONES_OCUPADAS: dict = {}


# ============================
# ===== FUNCIONES UTILES =====
# ============================

# Verificador simple de ruts
def VerificarRut(rut: str = None, retornar: bool = False) -> bool | str:
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
        return int( datos[0] )
        
    return True


def DefinirValor(asiento: int = None) -> int | None:
    if not asiento:
        print(1)
        return None
    
    if not ( asiento <= 100 or asiento >= 1 ):
        return None
    
    if asiento >= 51:
        return 50000, 3
    elif asiento >= 21:
        return 80000, 2
    else:
        return 120000, 1


# ============================
# ===== DEFINIR FUNCIONES ====
# ============================

def MostrarUbicaciones():
    print("X-----------------------------------------X")
    print("|                ESCENARIO                |")
    print("X-----------------------------------------X")
    
    # Anterior forma de mostrar valores
    #print(UBICACIONES.reshape(10, 10))
    
    # Nueva forma no floja de mostrar valores
    for x in range(1, 101):
        
        # Si el numero es una decena entonces se creara una nueva linea
        # En el caso contrario solo añadira un espacio
        # ESTA CUESTION LA APRENDI DEL GARRYS MOD XDDD
        # separador = x % 10 == 0 and "\n" or " "
        separator = "\n" if x % 10 == 0 else " "
        valor = UBICACIONES[x - 1]
        print(str(valor).rjust(3, " "), end=f"{separator}")
    
    print("[2] Los asientos marcados con X estan ocupados")
    


def ComprarEntradas():
    MostrarUbicaciones()
    
    while True:
        try:
            asiento = int( input("[1] Ingrese su asiento: ") )
            if asiento > 100 or asiento < 1:
                raise Exception
            elif UBICACIONES[asiento - 1] == "X":
                raise KeyError
        except ValueError:
            print("[1] Error: El asiento no es valido")
        except KeyError:
            print("[1] Asiento ocupado: El asiento ya esta siendo ocupado, porfavor seleccione otro")
        except Exception:
            print("[1] Error: El asiento no existe o esta fuera de rango")
        else:
            break
    while True:
        try:
            rut: str = input("[1] Ingrese su rut: ")
            if not VerificarRut(rut):
                raise Exception
            else:
                rut: int = VerificarRut(rut, retornar=True)
        except Exception:
            print("[1] Rut no valido: El rut ingresado no es valido")
        else:
            break
    
    UBICACIONES[asiento - 1] = "X"
    UBICACIONES_OCUPADAS[asiento] = rut
    print(f"[1] Asiento numero {asiento} comprado para {rut}")


def MostrarAgentes():
    print("==============================")
    print("========= ASISTENTES =========")
    print("==============================")
    print("")
    
    Ordenado = {}
    for x, y in sorted( UBICACIONES_OCUPADAS.items() ):
        Ordenado[y] = x

    for rut, asiento in sorted( Ordenado.items() ):
        print(f"[3] El asistente '{rut}' ocupa el asiento '{asiento}'")



def CalcularGanancias():
    Platinum: int = 0
    Gold: int = 0
    Silver: int = 0
    
    PlatinumCantidad: int = 0
    GoldCantidad: int = 0
    SilverCantidad: int = 0

    for i in UBICACIONES_OCUPADAS.keys():
        cantidad, tipo = DefinirValor(i)
        if tipo == 1:
            PlatinumCantidad += cantidad
            Platinum += 1
        elif tipo == 2:
            GoldCantidad += cantidad
            Gold += 1
        else:
            SilverCantidad += cantidad
            Silver += 1
    
    # Se que esto se puede optimizar, pero funciona y eso es lo que importa
    pc, gc, sc = str(PlatinumCantidad).rjust(7, " "), str(GoldCantidad).rjust(7, " "), str(SilverCantidad).rjust(7, " ")
    p, g, s = str(Platinum).rjust(8, " "), str(Gold).rjust(8, " "), str(Silver).rjust(8, " ")
    total, totalcantidad = str(Platinum + Gold + Silver).rjust(8, " "), str(PlatinumCantidad + GoldCantidad + SilverCantidad).rjust(7, " ")
    print(f"X======================X==========X===========X")
    print(f"|     Tipo Entrada     | Cantidad |   Total   |")
    print(f"X======================X==========X===========X")
    print(f"| Platinum - 120.000   | {p}  | ${pc} |")
    print(f"| Gold     -  80.000   | {g}  | ${gc} |")
    print(f"| Silver   -  50.000   | {s}  | ${sc} |")
    print(f"X======================X==========X===========X")
    print(f"| Total                | {total}  | ${totalcantidad} |")
    print(f"X======================X==========X===========X")

    

# ============================
# ===== CODIGO PRINCIPAL =====
# ============================

def Main():
    
    print("==============================")
    print("======== Creativos.cl ========")
    print("==============================")
    
    while True:
        print("")
        print("[1] Comprar entradas")
        print("[2] Mostrar ubicaciones disponibles")
        print("[3] Ver listado de agentes")
        print("[4] Mostrar ganancias totales")
        print("[5] Salir")
        print("")
        try:
            opcion = int( input("Seleccione una opcion: ") )
            if opcion > 5 or opcion < 1:
                raise Exception
        except ValueError:
            print("Error: Numero invalido o no es un numero, intente nuevamente")
        except Exception:
            print("Error: La opcion seleccionada no es valida")
        else:
            print("")
            if opcion == 1:
                ComprarEntradas()
            elif opcion == 2:
                MostrarUbicaciones()
            elif opcion == 3:
                MostrarAgentes()
            elif opcion == 4:
                CalcularGanancias()
            elif opcion == 5:
                print("Tenga un buen dia")
                print(" - Vicente Cortes  10-07-2023")
                exit()
Main()