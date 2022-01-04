def conversion(moneda, tasa):
  pesos = float(input(f'que cantidad de {moneda} quieres convertir?: '))
  cambio_dolar = tasa
  USD = str(round(pesos / cambio_dolar, 2))
  pesos = str(pesos)
  print (pesos + ' pesos es igual a ' + USD + ' dolares')


menu = """
Bienvenido a mi conversor de monedas, que moneda quieres convertir a dolar ?

1- Pesos colombianos
2- Pesos Mexicanos
3- Pesos Argentinos

digita un numero:
"""
opcion = int(input(menu))

if opcion == 1:
  conversion('Pesos Colombianos', 3462.11)
elif opcion == 2:
  conversion('Pesos Mexicanos', 19.81)
elif opcion == 3:
  conversion('Pesos Mexicanos', 85.73)
else:
  print ('opcion incorrecta, por favor ingresa una opcion correcta')

