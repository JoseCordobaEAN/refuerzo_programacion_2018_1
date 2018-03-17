# leemos los elementos y los guardamos en la lista
numeros = []

# Leemos el primer n
n = input("Ingrese un n\n")
numeros.append(n)

# Leemos el segundo n
n = input("Ingrese un n\n")
numeros.append(n)

# Leemos el tercer n
n = input("Ingrese un n\n")
numeros.append(n)

# Leemos el cuarto n
n = input("Ingrese un n\n")
numeros.append(n)

# Leemos el quinto n
n = input("Ingrese un n\n")
numeros.append(n)

# Acumulamos la suma
resultado = 0
for n in numeros:
    resultado += float(n)

# Imprimimos el resultado
print("La suma de sus numeros es",resultado)
