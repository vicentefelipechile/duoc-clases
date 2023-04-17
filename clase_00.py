# Calculadora

file = open("calculadora.py", "w")
file.write("num1: int = int( input('Ingrese numero 1: ') )\n")
file.write("num2: int = int( input('Ingrese numero 2: ') )\n\n")
file.write("suma: int = num1 + num2\n")

file.write(f"if suma == 0:\n")
file.write(f"   print('La suma total es ', suma)\n")

for x in range(1000):
    x=x+1
    file.write(f"elif suma == {x}:\n")
    file.write(f"   print('La suma total es', suma)\n")

file.write("\n\n")

for x in range(1000):
    x=x+1001
    file.write(f"elif suma == {x}:\n")
    file.write(f"   print('La suma total es', suma)\n")