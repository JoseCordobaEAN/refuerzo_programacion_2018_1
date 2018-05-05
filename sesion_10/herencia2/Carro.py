from sesion_10.herencia2.Vehiculo import Vehiculo

class Carro(Vehiculo):

    def __init__(self, cambios = 4, pasajeros = 4, ruedas = 4):
        """
        Crea un nuevo carro
        :param cambios: Los cambios del carro
        :param pasajeros: la cantidad de pasajeros
        :param ruedas: la cantidad de ruedas
        """

        Vehiculo.__init__(self,pasajeros)
        self.ruedas = ruedas
        self.cambios = cambios