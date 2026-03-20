def suma_posicion_par(lista, idx=0):
    if idx >= len(lista):
        return 0

    if idx % 2 == 0:
        return lista[idx] + suma_posicion_par(lista, idx+1)
    else:
        return suma_posicion_par(lista, idx+1)


# 0-based
# 1,3,5,7,9
print(suma_posicion_par([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
