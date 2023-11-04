def primo(numero):
    contador = 0


    for i in range(1, numero + 1):
      if i == 1 or i == numero:
        continue
      if numero % i == 0:
        contador += 1
    if numero == 1:
      return False
    elif contador == 0:
      return True
    else:
      return False

def main():
    numero = int(input("bienvenido al dectector de numeros primos, si quiere saber si tu numero es efectivamente primo puedes ingresarlo aqui: "))
    if primo(numero):
      print (f'{numero} es un numero primo')
    else:
      print (f'{numero} no es un numero primo')

if __name__ == "__main__":
    main()