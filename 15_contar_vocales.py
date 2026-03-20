def contar_vocales(texto):
    vocales = ['a', 'e', 'i', 'o', 'u']

    if len(texto) <= 0:
        return 0

    primera_letra = texto[0].lower()

    if primera_letra in vocales:
        return 1 + contar_vocales(texto[1:])
    else:
        return contar_vocales(texto[1:])


print(contar_vocales("Anita lava la tina"))
