def HolaMundo(nombre, emocion = "sin emocion", V1 = 0, V2 = 0):
    return f"hola {nombre} estoy {emocion} porque se que la operacion {V1}+{V2} es igual a {V1+V2}"
valor = [0, 1, 2 , 3, 4, 5, 6, 7, 8, input("ingresa un numero: \r\n")]
valor[9] = int(valor[9])
print(valor)
valor.pop(5) #elimina valor con la sexta posicion de la lista
print(valor)
valor.remove(0) #Busca el Valor "0" dentro de la lista y lo elimina de ella
print(valor)
if valor[7] % 2 == 0: #si el valor ingresado es par se eliminara el valor con la cuarta posicion
    print(f"{valor[7]} es par se procede a eliminar el cuarto valor de la lista")
    valor.pop(3)
print(valor)
if not 2 in valor: #si no se encuentra el valor "2" en la lista, se devuelve un true
    if 1 or 9 in valor: #si se encuentra el valor "1" o "9" en la lista se devuelve un true
        valor.remove(3) #se elimina el valor "3" de la lista
elif 1 in valor: #si en la lista se encuentra el valor "2" y el valor "1" se eliminara el segundo valor de la lista
    valor.pop(1)
print(valor)
hola_mundo = HolaMundo(input("cual es tu nombre?: \r\n"), "feliz", valor[0], valor[2])
print(hola_mundo.upper())
