n = int(input())

listas = 1
l = [0] * (n * 5)
trocas = 0
t = 0

for i in range(n * 5):
    l[i] = int(input())

while listas <= n:

    for i in range((n * 5) - ((n - 1) * 5)):
        for j in range((n * 5) - 1 - ((n - 1) * 5)):

            if listas <= 1:
                if (l[j] > l[j + 1]):
                    t = l[j]
                    l[j] = l[j + 1]
                    l[j + 1] = t
                    trocas = trocas + 1

            if listas > 1:
                if (l[j + ((listas - 1) * 5)] > l[j + 1 + ((listas - 1) * 5)]):
                    t = l[j + ((listas - 1) * 5)]
                    l[j + ((listas - 1) * 5)] = l[j + 1 + ((listas - 1) * 5)]
                    l[j + 1 + ((listas - 1) * 5)] = t
                    trocas = trocas + 1

    listas = listas + 1
    print(trocas)
    trocas = 0
