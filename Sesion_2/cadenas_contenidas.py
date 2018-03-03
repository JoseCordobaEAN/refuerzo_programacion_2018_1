# Solicitamos la cadena al usuario
cadena = input("Ingrese su cadena\n")

# Solicitamos la otra cadena al usuario
otra_cadena = input("Ingrese su otra cadena\n")

# Validamos si una cadena está contenida en la otra
if cadena in otra_cadena:
    print("La cadena",cadena,"esta en",otra_cadena)
else:
    print("La cadena",cadena,"no esta en",otra_cadena)
