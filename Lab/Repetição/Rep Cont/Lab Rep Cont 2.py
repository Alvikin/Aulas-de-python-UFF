for n in range(10000):
    n1 = n // 100
    n2 = n % 100
    if (n1 + n2) ** 2 == n and n >= 1000:
        print(n)
