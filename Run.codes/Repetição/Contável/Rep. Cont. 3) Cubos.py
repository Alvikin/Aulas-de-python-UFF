
for n in range(1000):
    n1 = n // 100
    n2 = (n // 10) % 10
    n3 = n % 10
    if ((n1 ** 3) + (n2 ** 3) + (n3 ** 3)) == n and n >= 100:
        print(n)
