# Solicitamos la primera cadena
cadena = input("¿Cual es su cadena? ")

# Solicitamos la cadena a verificar
cadena_interna = input("¿Cual es su cadena interna? ")

mensaje = "Su cadena " + cadena_interna + " esta contenida en " +cadena

#imprimimos si una esta contenida en la otra
print(mensaje, cadena_interna in cadena)
