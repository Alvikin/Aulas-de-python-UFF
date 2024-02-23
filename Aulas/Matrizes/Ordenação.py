n = int(input())
m = int(input())

A = []

for i in range(n):
    l = []
    for j in range(m):
        l.append(int(input()))
    A.append(l)

# cada linha
for k in range(n):
    # ordena linha por bolha
    for i in range(m):
        for j in range(m - 1):
            if (A[k][j] > A[k][j + 1]):
                t = A[k][j]
                A[k][j] = A[k][j + 1]
                A[k][j + 1] = t

for i in range(n):
    print(A[i])