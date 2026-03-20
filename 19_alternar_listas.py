def alternar_listas(lista1, lista2, idx=0):
    # Se asumen listas del mismo tamaño
    if len(lista1) != len(lista2):
        raise ValueError("Las listas deben ser del mismo tamaño")

    if len(lista1) <= 0:
        return []

    if idx >= len(lista1):
        return []

    return [lista1[idx], lista2[idx]] + alternar_listas(lista1, lista2, idx+1)


print(alternar_listas([1, 2, 3], ['a', 'b', 'c']))
