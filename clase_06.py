from os import system;system("cls")

print("============= EDADES =============")

personas: int = int( input("Ingrese cantidad de presonas: ") )
acumulado: int = 0
i: int = 0

while i != personas:
    edad: int = int( input(f"Ingrese la dedad de la persona {i+1}: ") )
    acumulado += edad
    i += 1

promedio: float = acumulado / personas

print(f"El promeio de edades es de: {promedio}")