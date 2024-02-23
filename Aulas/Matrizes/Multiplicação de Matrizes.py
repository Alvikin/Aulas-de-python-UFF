n = int(input('n ? '))
m = int(input('m ? '))
p = int(input('p ? '))

A = []
for i in range(n):
    l = []
    for j in range(m):
        l.append(int(input('A['+str(i)+','+str(j)+']: ')))
    A.append(l)

B = []
for i in range(m):
    l = []
    for j in range(p):
        l.append(int(input('B['+str(i)+','+str(j)+']: ')))
    B.append(l)

C = []
for i in range(n):
    C.append([0]*p)

for i in range(n):                    # percorre linhas
    for j in range(p):                # colunas da matriz c
        pe = 0                        # produto escalar da linha i de A
        for k in range(m):            # Pela coluna j de B
            pe = pe + A[i][k] * B[k][j]
        C[i][j] = pe

for i in range (n):
    print(C[i])
