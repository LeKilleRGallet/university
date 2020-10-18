

def HolaMundo(nombre, emocion = "sin emocion", a = 0, b = 0):
    return f"hola {nombre} estoy {emocion} porque se sumar {a} + {b} que es {a + b}"

hola_mundo = HolaMundo("mundo", "feliz", 2, 3)
print(hola_mundo.upper())