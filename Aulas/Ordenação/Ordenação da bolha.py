n = int(input())
l = [0] * n
t = 0

for i in range(n):
    l[i] = (int(input('num. ' + str(i) + ') ')))

for i in range(n):
    for j in range(n - 1):
        if (l[j] > l[j + 1]):
            t = l[j]
            l[j] = l[j + 1]
            l[j + 1] = t

print(l)
