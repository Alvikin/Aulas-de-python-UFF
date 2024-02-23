n1 = int(input())
n2 = int(input())
n3 = int(input())
soma = n1 + n2 + n3
if n1 != n2 and n1 != n3 and n2 != n3:
    print(soma)
elif n1 == n2 and n1 == n3:
    print('0')
elif n1 == n2:
    print(n3)
elif n1 == n3:
    print(n2)
elif n2 == n3:
    print(n1)
