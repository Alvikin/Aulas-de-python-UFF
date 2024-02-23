S = 0.0
a = 2
b = 3
n = 1

for i in range(1, 21, 1):
    if (i % 2 == 0):
        S = S - (a / b)
        print(i, ') -', a, ' / ', b,)
    else:
        S = S + (a / b)
        print(i, ') +', a, ' / ', b,)
    a = a + 4
    b = b + 1 + n
    n = n + 1

a = a + 4
b = b * 3
print('s = ', S)
