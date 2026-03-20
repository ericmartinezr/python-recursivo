def contar_pares(lista, idx=0):
    if idx >= len(lista):
        return 0

    if lista[idx] % 2 == 0:
        return 1 + contar_pares(lista, idx+1)
    else:
        return contar_pares(lista, idx+1)


print(contar_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
