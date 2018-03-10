# Solicitamos el nombre
nombre = input("¿Cual es su nombre?\n")

# Solicitamos la edad
edad = int(input("¿Cual es su edad?\n"))

# Solicitamos el Sexo
sexo = int(input('''¿Cual es su Sexo?
1. Femenino
2. Masculino
'''))

# Decidimos que hacer segun la edad
if sexo == 1:

    # Decidimos que hacer según el sexo
    if edad < 13:
        print("Hola niña",nombre)
    elif edad < 30:
        print("Hola señorita",nombre)
    else:
        print("Buenas Señora",nombre)
else:
    if edad < 13:
        print("Hola niñ0",nombre)
    elif edad < 30:
        print("Hola joven",nombre)
    else:
        print("Buenas Señor",nombre)
