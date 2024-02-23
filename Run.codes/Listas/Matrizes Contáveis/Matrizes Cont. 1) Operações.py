n = int(input())

A = []
tempA = []
B = []
C = []
l = []

for i in range(n):
    l = []
    for j in range(n):
        l.append(int(input()))
    A.append(l)

l = []

for i in range(n):
    l = [0] * n
    for j in range(n):
        l[j] = A[i][j]
    tempA.append(l)

for i in range(n):
    B.append([0] * n)

for i in range(n):
    C.append([0] * n)

for i in range(n):
    for j in range(n):
        for k in range(n):
            B[i][j] = B[i][j] + (A[i][k] * A[k][j])

for i in range(n):
    for j in range(n):
        A[i][j] = tempA[j][i]

for i in range(n):
    for j in range(n):
        C[i][j] = B[i][j] + A[i][j]

print(C)
