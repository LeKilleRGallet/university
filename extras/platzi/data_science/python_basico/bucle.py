def main():
  LIMITE = 1000000
  contador = 0
  potencia = 2**contador
  while potencia < LIMITE:
    print (f"2 elevado a {contador} es igual a: {potencia}")
    contador = contador + 1
    potencia = 2**contador

if __name__ == "__main__":
  main()