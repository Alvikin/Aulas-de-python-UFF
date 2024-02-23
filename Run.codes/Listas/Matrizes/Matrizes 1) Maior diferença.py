n = int(input())
m = int(input())

matriz = []

for i in range(n):
    linha = []
    for j in range(m):
        linha.append(int(input()))
    matriz.append(linha)

maior = matriz[0][0]

for i in range(n):
    for j in range(m):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        else:
            continue

for i in range(n):
    for j in range(m):
        matriz[i][j] = matriz[i][j] - maior

print(matriz)