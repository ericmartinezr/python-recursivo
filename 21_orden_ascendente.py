def verificar_orden_ascendente(lista):
    if len(lista) <= 1:
        return True

    if lista[0] > lista[1]:
        return False

    return verificar_orden_ascendente(lista[1:])


print(verificar_orden_ascendente([1, 2, 3, 4, 6, 5]))
