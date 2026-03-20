def eliminar_caracter(texto, caracter):

    if len(texto) <= 0:
        return ""

    if texto[0].lower() == caracter.lower():
        return "" + eliminar_caracter(texto[1:], caracter)
    else:
        return texto[0] + eliminar_caracter(texto[1:], caracter)


print(eliminar_caracter("Anita lava la tina", "a"))
