n = int(input())

matriz = []
media = 0
soma = 0
menor = 0

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input()))
    matriz.append(linha)

for i in range(n):
    for j in range(n):
        media = media + matriz[i][j]
media = media / (n * n)

for i in range(n):
    for j in range(1, n):
        if n - j > i:
            soma = soma + matriz[i][n - j]

print(soma)

for i in range(n):
    for j in range(n):
        if matriz[i][j] < media:
            menor = menor + 1

print(menor)
