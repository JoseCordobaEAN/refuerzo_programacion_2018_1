# Solicitamos el número al usuario
numero = int(input("Ingrese su número\n"))

# Validamos que el dividendo sea par
if numero % 2 == 0:
    print("El dividendo",numero,"es par")
else:
    print("El dividendo ",numero,"es impar")
