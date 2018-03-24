# La estructura de repeticion while nos permite iterar
# Hasta que una condicion sea falsa
mensaje = ""

# Este programa repite lo que digas hasta que digas para
while mensaje != 'para':
    mensaje = input("Soy un lorito, dime que decir o 'para' para salir")
    if mensaje != 'para':
        print(mensaje)


