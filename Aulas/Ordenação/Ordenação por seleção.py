n = int(input())
l = [0] * n
t = 0

for i in range(n):
    l[i] = (int(input('num. ' + str(i) + ') ')))

for i in range(n - 1):
    for j in range(i + 1, n):
        if (l[i] > l[j]):
            t = l[i]
            l[i] = l[j]
            l[j] = t
