def es_divisible(dividendo, divisor):
    """
    (int, int) -> boolean

    Decide si un numero es divisible entre otro

    >>> es_divisible(8, 2)
    True
    >>> es_divisible(7, 2)
    False

    :precondition divisor !=0

    :param dividendo: el dividendo de la operación
    :param divisor: el divisor de la operacion
    :return: true si el numero es divisible, false de lo contrario
    """
    return dividendo % divisor == 0

def es_primo(numero):
    """
    (int) -> boolean

    Determina si un número es primo

    >>> es_primo(13)
    True

    >>> es_primo(21)
    False

    >>> es_primo(7)
    True

    :param numero: el numero a evauar
    :return: True si el numero es primo, False de lo contrario
    """
    # Recorremos los numeros usando el patron contador
    divisores = 0
    for i in range (1, numero +1):
        if es_divisible(numero, i):
            divisores += 1

    return  2 == divisores

def son_amigos(numero_1, numero_2):
    """
    (int, int) -> boolean

    Decide si dos numeros son amigos

    >>> son_amigos(1, 2)
    False

    >>> son_amigos(220, 284)
    True

    >>> son_amigos(1184, 1210)
    True

    :param numero_1: el numero a evaluar
    :param numero_2: el segundo numero a evaluar
    :return: True si la suma de sus divisores es igual al otro
    """

    divisores_primero = 0
    for i in range(1, numero_1):
        if es_divisible(numero_1, i):
            divisores_primero += i

    divisores_segundo = 0
    for i in range(1, numero_2):
        if es_divisible(numero_2, i):
            divisores_segundo += i

    return divisores_primero == numero_2 and divisores_segundo == numero_1

# Definir una funcion sumatoria
def sumatoria(desde, hasta, funcion):
    """
    (int, int, function) -> num
    Calcula la sumatoria en el rango deseado

    >>> sumatoria(1, 10, lambda x : x)
    55
    >>> sumatoria(1, 100, lambda x : x)
    5050

    :param desde: el limite inicial del rango de la sumatoria
    :param hasta: el limite final del rango de la sumatoria
    :param funcion: la función a alicar en la sumatoria
    :return: el resultado de la sumatoria en el rango deseado
    """
    # Recorrer todos los numeros en el rango acumulandolos
    # Agregar la funcion en el recorrido
    resultado = 0
    for i in range(desde, hasta+1):
        resultado += funcion(i)
    return resultado

# Sumatoria general
def sumatoria_general(desde, hasta):
    """
    (int, int) -> int

    >>> sumatoria_general(1, 10)
    55
    >>> sumatoria_general(1, 100)
    5050

    Calcula la suamtoria en un rango determinado
    :param desde: el limite inferior
    :param hasta: el limite superior
    :return: el calculo de la sumatoria
    """
    return sumatoria(desde, hasta, lambda x : x)

# Sumatoria cuadrados
def cuadrado(num):
    """
    Eleva un numero al cuadrado

    >>> cuadrado(2)
    4
    >>> cuadrado(4)
    16

    :param num: el numero a elevar
    :return: el numero al cuadrado
    """
    return num * num
def sumatoria_cuadrados(desde, hasta):
    """
    (int, int) -> int

    >>> sumatoria_cuadrados(1, 3)
    14

    Calcula la suamtoria de cuadrados en un rango determinado

    :param desde: el limite inferior
    :param hasta: el limite superior
    :return: el calculo de la sumatoria
    """
    return sumatoria(desde, hasta, cuadrado)

# Sumatoria de raices cuadradas
def sumatoria_raices_cuadradas(desde, hasta):
    return sumatoria(desde, hasta, lambda x : x ** (1/2))

# Sumatoria de f(x) = 2 x + n
def sumatoria_polinomio(desde, hasta):
    return sumatoria(desde, hasta, lambda x : 2 * x + hasta)

# Sumatoria de f(x) = 2x² + 3x
def sumatoria_polinomio_2(desde, hasta):
    return sumatoria(desde, hasta, lambda x : 2 * x ** 2 + 3 * x)
