import random

def get_password():
  qwerty = "qwertyuiopasdfghjklzxcvbnm"
  alphabeth = []
  capital = []
  symbol = ['!', '?', '_', '&', '$', '#', 'í', 'ú', 'ë', 'ä', '*']
  number = []

  
  for i in qwerty:
    alphabeth.append(i)
    i = i.upper()
    capital.append(i)


  for i in range(0,10):
    i = str(i)
    number.append(i)


  allin = alphabeth + capital + symbol + number
  password = []


  for i in range(15):
    rdmpassword = random.choice(allin)
    password.append(rdmpassword)


  password = ''.join(password)
  return password

def main():
  password = get_password()
  print (f'tu nueva contraseña es {password}')


if __name__ == "__main__":
    main()