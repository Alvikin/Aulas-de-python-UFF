c3 = 0
tot = 0.0
for i in range(1,11,1):
    sal = float(input('salário ? '))
    cla = int(input('classe ?'))
    sal2 = 0.0
    nome = ''

    if (cla == 1):
        sal2 = 2 * sal
        nome = 'bom'

    if (cla == 2):
        sal2 = sal + sal / 2
        nome = 'médio'

    if (cla == 3):
        sal2 = salc3 = c3 + 1
        nome = 'nhé'

    tot = tot + sal2
    print('salário = ', sal2, 'classe = ', nome)
print('classe3 = ', c3, 'total = ', tot)
