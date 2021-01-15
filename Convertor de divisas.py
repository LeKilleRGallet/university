COP = input('que cantidad de pesos quieres convertir?: ')
COP = float(COP)
USDCOP = 3400
USD = COP / USDCOP
USD = round(USD, 2)
USD = str(USD)
COP = str(COP)
print (COP + ' pesos es igual a ' + USD + ' dolares')