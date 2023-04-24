
cantidad = int( input("Ingrese cantidad de personas: ") )
promedio = 0

for i in range(cantidad):
    i+=1

    edad = int( input(f"Ingrese su edad persona {i}: ") )
    promedio = promedio + edad


print(f"El promedio de edad es {promedio/cantidad}")