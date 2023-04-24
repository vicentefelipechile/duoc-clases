"""
Genere un convertidor de: 

⮚ Dólar australiano a pesos chilenos 
⮚ Peso Argentino a peso chileno 
⮚ Yen a pesos chilenos 

Considere que los valores son variables
"""
peso_chileno: float = 795.43

moneda_australiana: float = 1.49
moneda_argentina: float = 217.49
moneda_yen: float = 134.91

cantidad: float = float( input("Introduzca cantidad a convertir (800.00): ") )
cantidad = round(cantidad / peso_chileno, 2)

print(f"Total Dolar australiano:", round(cantidad / moneda_australiana, 2))
print(f"Total Peso Argentino:", round(cantidad / moneda_argentina, 2))
print(f"Total Yen:", round(cantidad / moneda_yen, 2))