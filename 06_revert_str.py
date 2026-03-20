def revertir_string(cad):
    if len(cad) == 0:
        return ""

    return cad[-1] + revertir_string(cad[:-1])


print(revertir_string("hola, como estas?"))
