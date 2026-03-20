def parentesis(texto):

    if len(texto) == 0:
        return True

    combinaciones_validas = ["()", '{}', "[]"]

    cc = texto[0] + texto[-1]
    if cc in combinaciones_validas:
        return parentesis(texto[1:-1])
    else:
        return False


print(parentesis("([()])"))
