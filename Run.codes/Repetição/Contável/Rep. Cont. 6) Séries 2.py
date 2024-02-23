x = int(input())
S = x
z = 3
y = 7

for i in range(1, 100, 1):

    if (i % 2 == 0):
        S = S - ((z * x) / y)
    else:
        S = S + ((z * x) / y)
    y = y + 2
    z = z + 5

print('%.3f' % S)
