def capitalizar_string(texto, idx=0):
    if len(texto) <= 0:
        return ""

    if idx >= len(texto):
        return ""

    if idx == 0:
        return texto[idx].upper() + capitalizar_string(texto, idx+1)
    elif texto[idx].lower() == " ":
        return f" {texto[idx+1].upper()}" + capitalizar_string(texto, idx+2)
    else:
        return texto[idx] + capitalizar_string(texto, idx+1)


print(capitalizar_string("anita lava la tina"))
