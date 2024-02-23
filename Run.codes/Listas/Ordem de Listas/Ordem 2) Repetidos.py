n = int(input())
# l = numeros inseridos que serão ordenados
l = [0] * n
# c = numeros inseridos ordenados sem repetições
c = []
t = 0
f = -1

for i in range(n):
    l[i] = int(input())

for i in range(n):
    for j in range(n - 1):
        if (l[j] > l[j + 1]):
            t = l[j]
            l[j] = l[j + 1]
            l[j + 1] = t

for i in range(n):
    for j in range(i + 1, n):
        if l[i] == f:
            break
        if l[i] == l[j]:
            f = l[i]
            c.append(l[i])
            break
        else:
            break

for i in range(n):
    for j in range(i + 1, n):
        if l[i] != l[j] and l[i] != l[j - 2]:
            c.append(l[i])
            break
        else:
            break

if l[len(l) - 1] != l[len(l) - 2]:
    c.append(l[len(l) - 1])

for i in range(len(c)):
    for j in range(len(c) - 1):
        if (c[j] > c[j + 1]):
            t = c[j]
            c[j] = c[j + 1]
            c[j + 1] = t

print(c)