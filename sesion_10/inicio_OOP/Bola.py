class Bola:
    """
    Representa una bola
    """

    def __init__(self, tamano, color):
        """
        Crea una nueva instancia de una Bola

        >>> Bola('pequeña', 'azul')
        Bola de tamaño pequeña y color azul

        :param tamano: El tamaño de la bola
        :param color: El color de la Bola
        """
        self.tamano = tamano
        self.color = color


    def __repr__(self):
        """
        Genera una respresentación en forma de cadena de nuestra
        Bola

        :return: str la representacion de la bola
        """
        return 'Bola de tamaño ' + self.tamano + \
               ' y color ' + self.color


    def __eq__(self, other):
        """
        Permite evaluar la igualdad entre dos bolas

        :param other: La otra bola para comparar
        :return: True si son iguales False de lo contrario
        """
        if isinstance(other,Bola):
            return self.color == other.color and \
                   self.tamano == other.tamano
        raise ValueError('No se pueden comparar Bolas con '
                         + type(other).__name__)

    def rodar(self):
        """
        Representa el movimiento de una bola

        Si la bola es grande rueda 20cm

        si no rueda 10cm

        :return: str con el movimiento de la bola
        """
        if self.tamano.lower() == 'grande':
            return "La bola rueda 20cm"
        return "La bola rueda 10cm"