def main():
  LIMITE = 1000000
  potencia = 0
  contador = 0
  while potencia < LIMITE:
    potencia = 2**contador
    print (f"2 elevado a {contador} es igual a {potencia}")
    contador = contador + 1

if __name__ == "__main__":
  main()