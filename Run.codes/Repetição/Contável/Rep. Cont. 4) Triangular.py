n = int(input())
for i in range(n):
    x1 = i
    x2 = x1 + 1
    x3 = x2 + 1
    if n == x1 * x2 * x3:
        print(x1)
        print(x2)
        print(x3)
        break
    if i == n - 1:
        print('não')
