# Leemos una cadena
cadena = input("Ingrese una cadena\n")
try:
    ultimo = cadena[-1]
    penultimo = cadena[-2]
    antepenultimo = cadena[-3]

    print("El ultimo elemento de la cadena es",ultimo,
          "\nEl penultimo elemento de la cadena es",penultimo,
          "\nEl antepenultimo elemento de la cadena es",antepenultimo)
except IndexError:
    print("La cadena",cadena,"no tiene suficientes elementos")
