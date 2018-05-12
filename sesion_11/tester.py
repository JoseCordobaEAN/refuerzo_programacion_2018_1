# importamos la clase de pruebas
from sesion_11.Encapsulada import Encapsulada

# Creamos una nueva instancia de nuestra clase encapsulada
encapsulada = Encapsulada()

# Imprimimos nuestro atributo visible
print(encapsulada.atributo_visible)

# Imprimimos nuestro atributo protegido
print(encapsulada._atributo_protegido)

# Intentamos imprimir nuestro atributo privado
try:
    print(encapsulada.__atributo_privado)
except AttributeError:
    print('No se pueden imprimir atributos privados')

# Imprimimos el atributo privado a través del
# metodo proporcionado
print(encapsulada.get_atributo_privado())

encapsulada.set_atributo_privado('Cambio privado')
print(encapsulada.get_atributo_privado())