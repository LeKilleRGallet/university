def HolaMundo(nombre, emocion = "sin emocion", V1 = 0, V2 = 0):
    return f"hola {nombre} estoy {emocion} porque se que la operacion {V1} + {V2} es igual a {V1 + V2}"
valor = [0, 1, 2 , 3, 4, 5, 6, 7, 8, 9]
valor.pop(2) #elimina valor con la primera posicion de la lista, dandole ahora a el Valor 1 la primera posicion
valor.remove(1) #Busca el Valor "1" dentro de la lista y lo elimina de ella
hola_mundo = HolaMundo("mundo", "feliz", valor[0], valor[2])
print(hola_mundo.upper())