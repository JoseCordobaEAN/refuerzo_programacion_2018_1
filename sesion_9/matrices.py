# Las matrices simplemente son listas de listas
matriz_A = [[1,2,3], [4,5,3], [7,8,3]]
print(matriz_A)

# Podemos imprimir cada uno de los vectores fila de la matriz
for fila in matriz_A:
    print(fila)

# Podemos imprimir todos los elementos de la matriz
for fila in matriz_A:
    for elemento in fila:
        print(elemento)

def vector_columna(matriz, columna):
    """
    (list of list, int) -> list

    Obtiene el vector columna para la posicion de la matriz

    >>> vector_columna([[1,2],[1,2]],0)
    [1, 1]

    >>> vector_columna([[1,2],[1,2]],1)
    [2, 2]

    :param matriz: la matriz que contiene nuestro vector
    :param columna: int la poscicion de la columna de nuestro vector
    :return: list con los elementos de la columna seleccionada
    """
    vector_resultante = []
    for fila in matriz:
        vector_resultante.append(fila[columna])
    return vector_resultante


def producto_punto(vector_a, vector_b):
    """
    (list, list) -> num

    calcula el producto escalar entre dos vectores

    >>> producto_punto([1,2], [1,2])
    5

    >>> producto_punto([2,2,2], [2,2,2])
    12

    :param vector_a: el primer vector
    :param vector_b: el segundo vector
    :return: num el escalar resultante
    """
    resultado = 0
    for i in range(0, len(vector_a)):
        resultado += vector_a[i] * vector_b[i]
    return resultado


def producto_matrices(matriz_A, matriz_B):
    """
    (list of list, list of list) -> list of list

    Realiza el producto de matrices

    >>> producto_matrices([[1,2], [3, 4]],[[1,2], [3, 4]])
    [[7, 10], [15, 22]]


    :param matriz_A:
    :param matriz_B:
    :return: list of list la matriz A * B
    """
    resultante = []
    for fila in matriz_A:
        fila_resultante = []
        for j in range(0, len(fila)):
            columna = vector_columna(matriz_B,j)
            escalar = producto_punto(fila, columna)
            fila_resultante.append(escalar)
        resultante.append(fila_resultante)
    return resultante