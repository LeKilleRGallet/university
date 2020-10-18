def HolaMundo(nombre, emocion = "sin emocion", V1 = 0, V2 = 0):
    return f"hola {nombre} estoy {emocion} porque se que la operacion {valor[1]} + {valor[2]} es igual a {valor[1] + valor[2]}"
valor = [0, 1, 2 , 3, 4, 5, 6, 7, 8, 9]
hola_mundo = HolaMundo("mundo", "feliz", valor[1], valor[2])
print(hola_mundo.upper())