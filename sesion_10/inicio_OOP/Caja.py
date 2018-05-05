class Caja:
    """
    Representa una Caja
    """

    def __init__(self, tamano, color):
        """
        Crea una nueva instancia de una Bola

        >>> Caja('pequeña', 'azul')
        Caja de tamaño pequeña y color azul

        :param tamano: El tamaño de la bola
        :param color: El color de la Bola
        """
        self.tamano = tamano
        self.color = color


    def __repr__(self):
        """
        Genera una respresentación en forma de cadena de nuestra
        Caja

        :return: str la representacion de la caja
        """
        return 'Caja de tamaño ' + self.tamano + \
               ' y color ' + self.color


    def __eq__(self, other):
        """
        Permite evaluar la igualdad entre dos Cajas

        :param other: La otra bola para comparar
        :return: True si son iguales False de lo contrario
        """
        if isinstance(other, Caja):
            return self.color == other.color and \
                   self.tamano == other.tamano
        raise ValueError('No se pueden comparar Cajas con '
                         + type(other).__name__)