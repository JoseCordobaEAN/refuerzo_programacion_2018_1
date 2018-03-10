# Intentamos Leer el año del usuario
try:
    ano = int(input("Ingrese su año a evaluar\n"))

    # Validamos que el año sea multiplo de 400
    if ano % 400 == 0:
        print("El año",ano,"es bisiesto")
    # Validamos que el no año sea multiplo de 100
    elif ano % 100 == 0:
        print("El año",ano,"no es bisiesto")
    # Validamos que el año sea multiplo de 4
    elif ano % 4 == 0:
        print("El año",ano,"es bisiesto")
    # Si el año no es ninguno de los casos anteriores
    else:
        print("El año",ano,"no es bisiesto")

# Manejamos el error en caso que nos den un dato invalido
except ValueError:
    print("No ha ingresado un año valido")

# print(ano)
