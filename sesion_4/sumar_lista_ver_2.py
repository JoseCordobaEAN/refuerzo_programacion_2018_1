# leemos los elementos y los guardamos en la lista
numeros = []

# Preguntamos cuantos datos queremos trabajar
cantidad_de_numeros = int(input("Cuantos numeros quiere agregar?\n"))

# Iteramos en el rango de numeros
for num in range (0, cantidad_de_numeros):
    numeros.append(float(input("ingrese un numero\n")))

# Acumulamos la suma
resultado = 0
for n in numeros:
    resultado += float(n)

# Imprimimos el resultado
print("La suma de sus numeros es",resultado)
