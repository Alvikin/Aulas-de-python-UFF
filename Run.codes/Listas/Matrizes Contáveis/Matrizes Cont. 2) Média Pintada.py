n = int(input())

A = []
media = 0
d = 0

for i in range(n):
    l = []
    for j in range(n):
        l.append(int(input()))
    A.append(l)

for i in range(n):
    for j in range(n):
        if i < n / 2:
            if j > i and j < n - i - 1:
                media = media + A[i][j]
                d = d + 1
        if i > n / 2:
            if j < i and j > n - i - 1:
                media = media + A[i][j]
                d = d + 1

print('%.2f' % (media / d))