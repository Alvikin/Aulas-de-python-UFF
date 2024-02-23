resp = 1
while resp == 1:
    x = int(input())
    a = 1
    b = 2
    s = 0

    if 1 <= x <= 2:
        if x == 1:
            print(a)
        if x == 2:
            print(a)
            print(b)

    if x > 2:
        print(a)
        print(b)
        for i in range(x - 2):
            s = (a * b) + 1
            print(s)
            a = b
            b = s
    resp = int(input())