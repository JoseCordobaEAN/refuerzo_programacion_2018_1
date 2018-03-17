# Leemos el texto del usuario
texto = input("¿Cual es su texto?\n")

# Contamos las vocales
vocales = 0
for letra in texto:
    if letra in "aeiouAEIOU":
        vocales +=1

# Imprimimos cuantas vocales y cuantas consonantes hay
print('En su texto hay', vocales, "vocales y", len(texto)-vocales, "consonantes")
