# Leemos los 5 numeros
numeros =[]
numeros.append(int(input("Digite un número\n")))
numeros.append(int(input("Digite un número\n")))
numeros.append(int(input("Digite un número\n")))
numeros.append(int(input("Digite un número\n")))
numeros.append(int(input("Digite un número\n")))

#print(numeros)

# Creamos la lista resultante
operaciones = []

# Hacemos las operaciones
operaciones.append(numeros[0] + numeros[1] + numeros[2]
                   + numeros[3] + numeros[4])
operaciones.append(numeros[0] - numeros[1] - numeros[2]
                   - numeros[3] - numeros[4])
operaciones.append(numeros[0] * numeros[1] * numeros[2]
                   * numeros[3] * numeros[4])
operaciones.append(numeros[0] // numeros[1] // numeros[2]
                   // numeros[3] // numeros[4])
operaciones.append(numeros[0] % numeros[1] % numeros[2]
                   % numeros[3] % numeros[4])

print(operaciones)
