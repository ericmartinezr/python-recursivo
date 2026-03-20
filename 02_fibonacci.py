def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# 9 = 0 + 1+ 1 + 2 +3 + 5 + 8 + 13 + 21


print(fibonacci(9))
