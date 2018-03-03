# Leemos el posible numero
numero = input("Ingrese un número: ")

#Intentamos convertirlo a dividendo
try:
    numero = float(numero)
    print("Su dividendo es", numero)
except ValueError:
    #Si no logramos convertirlo notificamos al usuario
    print(numero," no es un número")
