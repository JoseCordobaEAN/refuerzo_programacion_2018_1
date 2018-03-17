# leemos los elementos y los guardamos en la lista
numeros = []

# Preguntamos cuantos datos queremos trabajar
cantidad_de_numeros = int(input("Cuantos numeros quiere agregar?\n"))

# Iteramos en el rango de numeros
for num in range (0, cantidad_de_numeros):
    numeros.append(float(input("ingrese un numero\n")))

#contamos los positivos
positivos = 0
negativos = 0
for n in numeros:
    if float(n)>=0:
        positivos +=1
    else:
        negativos +=1

print("en la lista", numeros, " hay", positivos, "numeros positivos y", negativos,"Negativos")
