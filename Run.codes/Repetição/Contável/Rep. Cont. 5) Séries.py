n = int(input())
s = 0
a = 1

for i in range(1, 51, 1):
    if i % 2 == 0:
        s = s + (a * n)
    else:
        s = s + (a + n)
    a = a + 4

print(s)
