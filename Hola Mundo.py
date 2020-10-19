def HolaMundo(nombre, emocion = "sin emocion", V1 = 0, V2 = 0):
    return f"hola {nombre} estoy {emocion} porque se que la operacion {V1}+{V2} es igual a {V1+V2}"
valor = [0, 1, 2 , 3, 4, 5, 6, 7, 8, 9]
print(valor)
valor.pop(2) #elimina valor con la tercera posicion de la lista, dandole ahora a el Valor 3 la tercera posicion
print(valor)
valor.remove(0) #Busca el Valor "0" dentro de la lista y lo elimina de ella
print(valor)
if valor[0] == 1: #si el valor con la primera posicion es "1" entonces se eliminara el valor con la cuarta posicion de la lista
    valor.pop(3)
print(valor)
if not 2 in valor: #si no se encuentra el valor "2" en la lista, se devuelve un true
    if 1 in valor: #si se encuentra el valor "1" en la lista se devuelve un true
        valor.remove(3) #se elimina el valor "3" de la lista
print(valor)
hola_mundo = HolaMundo("mundo", "feliz", valor[0], valor[2])
print(hola_mundo.upper())
