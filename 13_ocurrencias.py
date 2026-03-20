def ocurrencias(texto, caracter):
    if len(texto) <= 0:
        return 0

    if texto[0] == caracter:
        return 1 + ocurrencias(texto[1:], caracter)
    else:
        return ocurrencias(texto[1:], caracter)


print(ocurrencias("tres tristes tigres trigaban en un trigal", "t"))
