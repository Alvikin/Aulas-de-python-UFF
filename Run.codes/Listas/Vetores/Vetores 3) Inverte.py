n = int(input())
a = []
c = [0] * n
fatorial = 1
for i in range(n):
    c[i] = int(input())

for i in range(-1,-n - 1,-1):
    a.append(int((c[i])))

for i in range(n):
    if a[i] == 0:
        a[i] = 1
        continue
    for j in range(1,a[i] + 1):
        if a[i] > 2:
           fatorial = fatorial * j
           if j == a[i]:
               a[i] = fatorial
               fatorial = 1
               break
print(a)