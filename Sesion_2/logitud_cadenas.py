# Solicitamos la cadena al usuario
cadena = input("Ingrese su cadena\n")

# Solicitamos la otra cadena al usuario
otra_cadena = input("Ingrese su otra cadena\n")

# Calculamos la longitud de la cadena
longitud_cadena = len(cadena)

# Calculamos la longitud de la otra cadena
longitud_otra_cadena = len(otra_cadena)

# Decidimos si miden lo mismo
if longitud_cadena == longitud_otra_cadena:
    print("Las 2 cadenas miden",longitud_cadena)
else:
    print("La cadena mide", longitud_cadena,
          "la otra cadena mide",longitud_otra_cadena)
