def potencia(num, pot):
    if pot == 0:
        return 1

    return num * potencia(num, pot - 1)


# 2^3 = 2*2*2
print(potencia(2, 10))
