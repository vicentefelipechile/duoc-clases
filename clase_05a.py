from os import system;system("cls")
"""
Una empresa de transporte requiere automatizar sus procesos
de calculo para poder cobrar por la entidad de paquetes que
trae un cliente.
Para calcular el valor total a cobrar y catalogarlo para 
envio, requiere preguntar el peso de cada bulto y determin-
ar el total segun lo siguiente:

  Kilos |   Categoria   |   Valor
   0-5       Liviano        $1000
   6-10      Normal         $4500
  11-20      Pesado         $8000
"""


def Frase(categoria: str = None) -> str:
    if not categoria:
        return

    catgoria = categoria.lower()
    largo = categoria.__len__()
    primerLetra = categoria[0]
    ultimaLetra = categoria[-1]

    if not ( largo == 7 or largo == 6):
        return 0

    if primerLetra == "l" and ultimaLetra == "o":
        return 1
    elif primerLetra == "n" and ultimaLetra == "l":
        return 2
    elif primerLetra == "p" and ultimaLetra == "o":
        return 3
    
    return 0


def Peso(peso: int = 0) -> int:
    if peso == 0:
        return
    
    if peso > 20:
        return 0
    elif peso < 0:
        return 0
    elif peso < 6:
        return 1
    elif peso < 11:
        return 2
    else:
        return 3

print("==============================================")
print("============== Fleterias Fletes ==============")
print("==============================================")
print("Bienvenido a Fleterias fletes: ")

cantidad: int = int( input("Ingrese cantidad de bultos que desea llevar: ") )

prod_liviano: int = 0
prod_normal: int = 0
prod_pesado: int = 0

print("""
  Kilos |   Categoria   |   Valor
   0-5       Liviano        $1000
   6-10      Normal         $4500
  11-20      Pesado         $8000
""")

i: int = 1
tipo: int = 0
while i <= cantidad:

    categoria = input(f"Ingrese categoria/peso del bulto {i}: ")
    if categoria.isdigit():
        categoria = int(categoria)
        tipo = Peso(categoria)
    else:
        categoria = categoria.lower()
        tipo = Frase(categoria)

    if tipo == 1:
        prod_liviano += 1
    elif tipo == 2:
        prod_normal += 1
    elif tipo == 3:
        prod_pesado += 1
    else:
        print("Error: Categoria no valida/no encontrada, porfavor, escriba bien su categoria")
        i -= 1
    
    i += 1

print("===============================")
print("========= ENCOMIENDAS =========")
print("===============================")
print(f"{prod_liviano} bulto LIVIANO:  ${prod_liviano*1000}")
print(f"{prod_normal} bulto NORMAL:   ${prod_normal*4500}")
print(f"{prod_pesado} bulto PESADO:   ${prod_pesado*8000}")
total: int = prod_liviano * 1000 + prod_normal * 4500 + prod_pesado * 8000
print("===============================")
print(f"   Total: ${total}")