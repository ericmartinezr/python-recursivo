# xAAxAxAAxAAxAx"

def ocurrencias_pares(texto):

    if len(texto) <= 1:
        return 0

    if texto[0] == texto[1]:
        return 1 + ocurrencias_pares(texto[1:])
    else:
        return ocurrencias_pares(texto[1:])


print(ocurrencias_pares("xAAxAxAAxAAxAxBxBBB"))
