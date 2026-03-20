def es_palindromo(pal):
    # Palindromo es una palabra que se lee igual al revés y al derecho
    # Por ej: Reconocer, al revés, es reconocer
    if len(pal) <= 1:
        return True

    if pal[0] != pal[-1]:
        return False

    return es_palindromo(pal[1:-1])


print(es_palindromo("reconocer"))
print(es_palindromo("Hola"))
