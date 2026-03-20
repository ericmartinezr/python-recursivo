def minimo_lista(lista):

    # Caso base
    if len(lista) == 1:
        return lista[0]

    # Minimo del resto
    min_resto = minimo_lista(lista[1:])

    # Comparar
    if lista[0] < min_resto:
        return lista[0]
    else:
        return min_resto


print(minimo_lista([2, 2, 3, 4, 10, 5, 6, 7, 8]))
