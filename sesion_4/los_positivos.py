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

#contamos los positivos
positivos = 0
negativos = 0
for n in numeros:
    if float(n)>=0:
        positivos +=1
    else:
        negativos +=1

print("en la lista", numeros, " hay", positivos, "numeros positivos y", negativos,"Negativos")
