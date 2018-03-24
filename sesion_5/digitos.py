# Vamos a convertir un numero entero en una lista de sus digitos
numero = int(input('Dime tu numero\n'))
digitos =[]
while numero !=0:
    digitos.insert(0,numero%10)
    numero //= 10

print('Los digitos de su numero son',digitos)
