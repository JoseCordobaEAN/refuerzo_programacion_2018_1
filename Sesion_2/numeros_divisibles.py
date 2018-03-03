# Leemos el posible dividendo
dividendo = input("Ingrese el dividendo: ")

#Intentamos convertirlo a número
try:
    dividendo = int(dividendo)
    # print("Su dividendo es", dividendo)

    # Leemos el posible divisor
    divisor = input("Ingrese el divisor: ")

    #Intentamos convertirlo a número
    try:
        divisor = int(divisor)

        #Validamos si dividendo es divisible entre divisor
        if(dividendo%divisor==0):
            print(dividendo,"es divisible entre",divisor)
        else:
            print(dividendo,"no es divisible entre",divisor)
    # Si no es un número notificamos
    except:
        print(divisor, "no es un número")
except ValueError:
    print(dividendo, "no es un número")
