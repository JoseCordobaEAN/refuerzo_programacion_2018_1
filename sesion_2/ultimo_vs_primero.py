# Leemos las dos cadenas
primera = input("Ingrese su primer cadena\n")
segunda = input("Ingrese su segunda cadena cadena\n")

# Intentamos obtener las cadenas
try:
    # Obtenemos el ultimo elemento de la primera
    ultimo_primera = primera[-1]

    # Obtenemos el primer elemento de la segunda
    primero_segunda = segunda[0]

    # Comparamos el ultimo elemento de la primera contra
    # El primero de la segunda
    if  ultimo_primera == primero_segunda :
        print('El ultimo elemento de la cadena',primera,
              'es igual al primer elemento de la cadena',segunda)
    else:
        print('El ultimo elemento de la cadena',primera,
              'es diferente al primer elemento de la cadena',segunda)

except IndexError:
    print("Las cadenas no pueden estar vacias")
