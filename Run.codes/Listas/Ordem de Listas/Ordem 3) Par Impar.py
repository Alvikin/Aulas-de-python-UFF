n = int(input())
l = [0] * (n)
par = []
impar = []
t = 0
c = []

for i in range(n):
    l[i] = int(input())

for i in range(n):
    if l[i] % 2 == 0 or l[i] == 0:
        par.append(l[i])
    else:
        impar.append(l[i])

for i in range(len(par) - 1):
    for j in range(i + 1, len(par)):
        if (par[i] > par[j]):
            t = par[i]
            par[i] = par[j]
            par[j] = t

for i in range(len(impar) - 1):
    for j in range(i + 1, len(impar)):
        if (impar[i] < impar[j]):
            t = impar[i]
            impar[i] = impar[j]
            impar[j] = t

c = par + impar

print(c)