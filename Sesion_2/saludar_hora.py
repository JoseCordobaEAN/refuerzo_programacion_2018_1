# Preguntamos la hora al usuario
hora = int(input("¿Que hora es? \n"))

# Saludamos de acuerdo con la hora
if hora < 12:
    print("Buenos días")
elif hora >= 12 and hora < 19:
    print("Buenas Tardes")
else:
    print("Buenas noches")

# La identación marca el alcance de nuestra estructura de decisión
print("Esto ocurre por fuera del if")
