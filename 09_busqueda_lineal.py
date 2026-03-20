def busqueda_lineal(lista, texto, idx=0):
    # Si el indice es igual o superior al largo de la lista
    # retornamos -1 ya que no se encontro el valor
    if idx >= len(lista):
        return "No encontrado"

    # El valor se encontro, lo devolvemos
    if lista[idx] == texto:
        return lista[idx]

    return busqueda_lineal(lista, texto, idx + 1)


print(busqueda_lineal(["Hola", "como", "estas"], "estas"))
