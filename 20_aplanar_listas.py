def aplanar_lista(lista):

    # [1, [2, [3, 4]], 5] → [1,2,3,4,5]

    if len(lista) <= 0:
        return []

    if isinstance(lista[0], list):
        return aplanar_lista(lista[0]) + aplanar_lista(lista[1:])
    else:
        return [lista[0]] + aplanar_lista(lista[1:])


print(aplanar_lista([1, 2, [3, 4, [5], [6, 7, 8]]]))
