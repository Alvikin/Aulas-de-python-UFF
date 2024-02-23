resp = 1
while resp == 1:
    n = int(input('n = '))
    x = 0
    a = 2
    b = 5
    c = 8

    if 1 <= n <= 3:
        if n == 1:
            print(a)
        if n == 2:
            print(a)
            print(b)
        if n == 3:
            print(a)
            print(b)
            print(c)

    if n > 3:
        print(a)
        print(b)
        print(c)
        for i in range(0, n - 3, 1):
            x = c - (a + b)
            print(x)
            a = b
            b = c
            c = x
    print('Quer usar outro n ?')
    resp = int(input('1-Sim 2-Não '))
