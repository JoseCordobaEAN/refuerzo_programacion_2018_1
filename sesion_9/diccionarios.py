# Un diccionario es una coleccion donde los elementos se
# Relacionan de la forma llave valor
# Creemos un diccionario facho :'(
mi_diccionario = {'castrochavismo':'castro mas chavismo',
                  'mamerto':'izquierdoso',
                  'petro':'El coco'}

# Podemos acceder a los elementos de nuestro diccionario
# usando la llave asociada
print(mi_diccionario['petro'])

# Podemos agregar nuevos elementos
mi_diccionario['uribe'] = 'el mejor presidente duelale a quien le duela'

# Podemos iterar sobre un diccionario
for llave in mi_diccionario:
    print('la llave',llave,'representa',mi_diccionario[llave])