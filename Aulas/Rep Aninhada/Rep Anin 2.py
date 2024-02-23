resp = 1
while resp == 1:
    x = int(input('x = '))
    s = x
    a = 4
    b = 2
    c = 2

    for i in range(1, 20, 1):
        s = s + (a * (x ** b) / c)
        print('(', a, '*', x, '**', b, ') /',c)
        a = a + 5
        b = b + 1
        c = 2 * c + 1
    print('s = ',s)
    resp = int(input('De novo ? (1) - Sim  (0) - Não'))
