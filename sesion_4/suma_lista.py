# leemos los elementos y los guardamos en la lista
numeros = []

# Leemos el primer numero
numero = input("Ingrese un numero\n")
numeros.append(numero)

# Leemos el segundo numero
numero = input("Ingrese un numero\n")
numeros.append(numero)

# Leemos el tercer numero
numero = input("Ingrese un numero\n")
numeros.append(numero)

# Leemos el cuarto numero
numero = input("Ingrese un numero\n")
numeros.append(numero)

# Leemos el quinto numero
numero = input("Ingrese un numero\n")
numeros.append(numero)

# Acumulamos la suma
resultado = 0
for numero in numeros:
    resultado += float(numero)

# Imprimimos el resultado
print("La suma de sus numeros es",resultado)
