lista = [0] * 11
iguais = []
elem = -1

for i in range(10 + 1):
    lista[i] = int(input())
    if i == 10:
        elem = lista[i]

for j in range(10):
    if lista[j] == elem:
        iguais.append(j)

print(iguais)