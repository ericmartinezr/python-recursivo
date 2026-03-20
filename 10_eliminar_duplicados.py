def eliminar_duplicados(lista):
    # Caso base
    if not lista:
        return []

    primero = lista[0]

    # Eliminar todas las apariciones del primero en el resto
    resto_sin_primero = [x for x in lista[1:] if x != primero]

    # Construir resultado
    return [primero] + eliminar_duplicados(resto_sin_primero)


print(eliminar_duplicados(["hola", "hola", "como estas", "hola"]))
