import random

def main():
  NAleatorio = random.randint(1, 100)
  Ningresado = int(input('adivina que numero pense del 1 al 100: '))
  while NAleatorio != Ningresado:
    if Ningresado < NAleatorio:
      print ('sigue intentando, ingresa un numero mayor')
    else:
      print ('sigue intentando, ingresa un numero menor')
    Ningresado = int(input(" "))
  print (f'{Ningresado} es el numero correcto')

if __name__ == "__main__":
    main()