# Para crear una lista usamos un nombre en plural
# y definimos los elementos usando []
licores = []
print(licores)
licores = ['tequila', 'cerveza', 'wiskey', 'Guaro']

# Podemos Imprimir nuestra lista
print(licores)

# Podemos Acceder a los elementos de la lista con su indice
licor_favorito = licores[0]

print(licor_favorito)

# Podemos acceder a los elementos de la lista desde el ultimo
# Utilizando números negativos
licor_menos_rico = licores[-1]

print(licor_menos_rico)

# Las listas son tipos de datos mutables, por lo tanto podemos
# Alterar sus elementos
licores[-1] = 'ron'
print(licores[-1])
print(licor_menos_rico)

# Podemos añadir elementos a nuestas listas
licores.append(licor_menos_rico)
print(licores)

# Podemos añadir un elemento en una posicion dada
licores.insert(1,'pisco')
print(licores)

# Podemos eliminar elementos de la lista utilizando la función
# remove()
licores.remove("Guaro") #Puedo usar variables licores.remove(licor_menos_rico)
print(licores)

# Podemos eliminar elementos utilizando la función pop()
ultimo_licor = licores.pop()
print(licores,ultimo_licor)

# Podemos remover un elemento dado su indice usando pop(num)
tercer_licor = licores.pop(2)
print(licores,tercer_licor)

# Podemos ordenar los elementos de una lista
# licores.sort()
# Mejor ordenamos una copia de la lista con sorted
licores_ordenados = sorted(licores)
print(licores_ordenados,licores)

# Podemos revertir una lista
licores_ordenados.reverse()
print(licores_ordenados)

# Podemos averiguar la longitud de una lista
longitud_licores = len(licores)
print("Tengo",longitud_licores,"licores")
