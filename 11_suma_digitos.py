def suma_digitos(num):
    # Ultimo digito
    if num <= 0:
        return 0

    return (num % 10) + suma_digitos(num // 10)


print(suma_digitos(25))
