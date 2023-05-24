from os import system;system("cls")
# En el gimnasio una trotadora es ampliamente utilizada,
# se requiere saber la cantidad de usuarios que utilizan
# la máquina de acuerdo a su edad y género, para esta estadística
# solo interesan los usuarios que están entre 18 y 25 años.
# Se debe mostrar la cantidad de Mujeres que utilizan la trotadora
# durante un día.

def genero(valor: str) -> int:
    if not valor:
        return 0

    valor = valor.lower()

    match valor:
        case "masculino":
            return 1
        case "femenino":
            return 2
        case "hombre":
            return 1
        case "mujer":
            return 2
    
    return 0




i: int = 0
mujeres: int = 0
hombres: int = 0
while True:
    i += 1

    print("")
    print(f"======= PERSONA {i} =======")
    g_genero: int = int( input(f"Ingrese su edad: ") )
    g_sexo: str = input(f"Ingrese su genero: ")
    
