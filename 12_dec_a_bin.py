def decimal_a_binario(n):
    # Caso base
    if n < 2:
        return str(n)

    # Caso recursivo
    return decimal_a_binario(n // 2) + str(n % 2)


print(decimal_a_binario(10))
