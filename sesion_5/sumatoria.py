# Leemos el numero del usuario
numero = int(input('Ingrese su numero\n'))

# Creamos un acumulador para guardar la sumatoria y un contador
resultado = 0
contador = 1

# Mientras mi contador sea menor o igual que el numero
while contador <= numero:
    resultado += contador
    contador+=1

# Imprimimos el resultado
print('el resultado de la sumatoria es', resultado)
