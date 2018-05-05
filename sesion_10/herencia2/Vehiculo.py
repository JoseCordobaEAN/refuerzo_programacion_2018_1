class Vehiculo:
    """
    Representa un vehiculo
    """

    def __init__(self, pasajeros = 1):
        """
        Crea una nueva instancia del vehiculo
        """
        self.pasajeros = pasajeros

    def __repr__(self):
        return 'Vehiculo para ' + str(self.pasajeros) + ' pasajeros'