COP = float(input('que cantidad de pesos quieres convertir?: '))
USDCOP = 3400
USD = str(round(COP / USDCOP, 2))
COP = str(COP)
print (COP + ' pesos es igual a ' + USD + ' dolares')