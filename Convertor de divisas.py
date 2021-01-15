menu = """
Bienvenido a mi conversor de monedas, que moneda quieres convertir a dolar ?

1- Pesos colombianos
2- Pesos Mexicanos
3- Pesos Argentinos

digita un numero:
"""
opcion = int(input(menu))

if opcion == 1:
  COP = float(input('que cantidad de pesos quieres convertir?: '))
  USDCOP = 3462.11
  USD = str(round(COP / USDCOP, 2))
  COP = str(COP)
  print (COP + ' pesos es igual a ' + USD + ' dolares')
elif opcion == 2:
  MXN = float(input('que cantidad de pesos quieres convertir?: '))
  USDMXN = 19.81
  USD = str(round(MXN / USDMXN, 2))
  MXN = str(MXN)
  print (MXN + ' pesos es igual a ' + USD + ' dolares')
elif opcion == 3:
  ARS = float(input('que cantidad de pesos quieres convertir?: '))
  USDARS = 85.73
  USD = str(round(ARS / USDARS, 2))
  ARS = str(ARS)
  print (ARS + ' pesos es igual a ' + USD + ' dolares')
else:
  print ('opcion incorrecta, por favor ingresa una opcion correcta')

