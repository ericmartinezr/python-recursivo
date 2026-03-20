def maximo_lista(lista):

    # Caso base
    if len(lista) == 1:
        return lista[0]

    # Máximo del resto
    max_resto = maximo_lista(lista[1:])

    # Comparar
    if lista[0] > max_resto:
        return lista[0]
    else:
        return max_resto


print(maximo_lista([1, 2, 3, 4, 10, 5, 6, 7, 8]))
