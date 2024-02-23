a = int(input('a = '))
b = int(input('b = '))

for i in range(a, b + 1, 1):
    cont = 0
    for j in range(2, i, 1):
        if(i % j == 0):
            cont = cont + 1
    if (cont == 0) and (i != 1):
        print(i)
