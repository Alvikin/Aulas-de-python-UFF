n = int(input())
m = int(input())
a = [0] * n
b = [0] * m
c = []
conta = 0
contb = 0

for i in range(n):
    a[i] = int(input())

for i in range(m):
    b[i] = int(input())

for i in range(0,n + m,1):

    if i == 0:
        c.append(a[conta])
        conta = conta + 1
        continue
    if i % 2 != 0 and contb < conta:
        c.append(b[contb])
        contb = contb + 1
        continue
    if i % 2 == 0 and conta <= (len(a) - 1):
        c.append(a[conta])
        conta = conta + 1
        continue
    else:
        c.append(b[contb])
        contb = contb + 1
        continue
print(c)