# Debemos importar nuestra clase para poder instaniar objetos
from sesion_10.inicio_OOP.Bola import Bola
from sesion_10.inicio_OOP.Caja import Caja

# Creamos un nuevo objeto llamando la funcion constructora
bola_1 = Bola('Grande', 'Negra')

# Podemos imprimir una representación del objeto
print(bola_1)

# O también podemos acceder a los atributos del mismo
print('El tamaño de la bola es',bola_1.tamano)
print('El color de la bola es',bola_1.color)

# Podemos crear otra instancia de una misma clase
bola_2 = Bola('Grande', 'Negra')

print(bola_1 == bola_2)

# Podemos crear diferentes instancias de objetos
caja = Caja('Grande', 'Negra')
print(caja)

# Aunque tienen atributos iguales Bolas y cajas deben ser diferentes
# print(bola_1 == caja)

# Podemos tambien llamar metodos (acciones en nuestros objetos
print(bola_1.rodar())