def abs2(numero):
    """
    (num) -> num

    Calcula el valor absoluto de un número

    >>> abs2(10)
    10
    >>> abs2(-8)
    8
    >>> abs2(0)
    0

    :param numero: el numero a evaluar
    :return: el valor absoluto del número
    """
    if numero < 0:
        # La palabra clave return se utiliza para retonar el resultado de
        # Nuestra función
        return -numero
    return numero

def potencia(base, exponente):
    """
    (num, num) -> num

    Calclula la potencia dada una base y un exponente

    >>> potencia(2,3)
    8
    >>> potencia(2,8)
    256
    >>> potencia(5,3)
    125

    :param base: la base de la operacion
    :param exponente: la cantidad de veces que se debe multiplicar por si mismo
    :return: el resultado de base elevado al exponente
    """
    return base ** exponente

def es_par(numero):
    """
    (num) -> boolean

    Valida si un numero es par

    >>> es_par(10)
    True
    >>> es_par(20)
    True
    >>> es_par(189)
    False

    :param numero: el numero a evaluar
    :return: True si el numero es par, False de lo contrario
    """
    return numero % 2 == 0

# Una función puede ser llamada dentro de otra
def es_impar(numero):
    """
    (num) -> boolean
    Determina si un numero es impar

    >>> es_impar(3)
    True
    >>> es_impar(8)
    False

    :param numero: el número a evaluar
    :return: True si es impar, false de lo contrario
    """
    return not es_par(numero)

def es_divisible(dividendo, divisor):
    """
    (int, int) -> boolean
    Determina si un numero es divisible entre otro

    >>> es_divisible(10,2)
    True
    >>> es_divisible(5,4)
    False

    :param dividendo: el primer numero
    :param divisor: el segundo nuemero
    :return: True si es divisible, False de lo contrario
    """
    return dividendo % divisor == 0