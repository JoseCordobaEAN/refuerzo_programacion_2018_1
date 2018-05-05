from sesion_10.herencia2.Vehiculo import Vehiculo
from sesion_10.herencia2.Carro import Carro


# Podemos utilzar parametros opcionales en el constructor
vehiculo_1 = Vehiculo()
print(vehiculo_1)
vehiculo_2 = Vehiculo(10)
print(vehiculo_2)

# Podemos Crear nuestro carro
carro_1 = Carro(pasajeros=6)
print(carro_1)