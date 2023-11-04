def palindromo(palabra):
  n_palabra = palabra.replace(' ', '')
  #print (n_palabra)
  n_palabra = n_palabra.lower()
  #print (n_palabra)
  i_palabra = n_palabra[::-1]
  #print (i_palabra)

  if n_palabra == i_palabra:
    return True
  else:
    return False


def main():
  palabra = input("ingresa un palindromo: ")
  es_palindromo = palindromo(palabra)
  if es_palindromo == True:
    print (f"{palabra} es un palindromo")
  else:
    print (f"{palabra} no es un palindromo")


if __name__ == "__main__":
    main()