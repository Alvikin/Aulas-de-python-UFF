a = int(input())
b = int(input())
for i in range(a, b + 1, 1):
    for h in range(1, b + 1, 1):
        if i == 1:
            break
        if h != i and h != 1:
            if i % h == 0:
                break
        elif h == i:
            print(i)
            break
