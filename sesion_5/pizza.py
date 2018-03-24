# Vamos a leer los ingredientes que quiere en la pizza el usuario
print("Hola, vamos a prepar tu pizza")
pizza = []

# Leemos los ingredientes usando while
while True:
    ingrediente = input("Dime tu ingrediente o di 'gracias' cuando"
                        "no quieras mas\n")
    if ingrediente == 'gracias':
        break
    else:
        pizza.append(ingrediente)

# Le preparamos una pizza al cliente
print('Te preparamos una rica pizza con')

# Sacamos los ingredientes de la pizza
while len(pizza)>0:
    print('La pizza tiene', pizza.pop())
