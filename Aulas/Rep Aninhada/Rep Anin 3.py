n = int(input('n = '))
s = 0
a = 2
b = 1

for i in range(n):
    f = 1
    for j in range(2, b + 1, 1):
        f = f * j
    print(a, '/', f)

    s = s + (a / f)
    a = a * 2
    b = b + 3

print('s = ',s)