n = int(input())
m = int(input())

tam = (n * m)
v = [0] * tam

l = []
matriz = []
for i in range(n):
    l = []
    for j in range(m):
        l.append(int(input()))
    matriz.append(l)

x = 0
for i in range(n):
    for j in range(m):
        v[x] = matriz[i][j]
        x = x + 1

for i in range(tam):
    for j in range(tam - 1):
        if v[j] < v[j + 1]:
            t = v[j]
            v[j] = v[j + 1]
            v[j + 1] = t

x = 0
for i in range(m):
    for j in range(n):
        matriz[j][i] = v[x]
        x = x + 1

print(matriz)