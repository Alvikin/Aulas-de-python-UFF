import random
d1 = int(input())
d2 = int(input())
d3 = int(input())
#d1 = random.randint(1, 6)
#d2 = random.randint(1, 6)
#d3 = random.randint(1, 6)
#123 132 231 213 321 312
if (d1 + 1 == d2 and d1 + 2 == d3) or (d1 + 2 == d2 and d1 + 1 == d3) or (d2 + 1 == d1 and d2 + 2 == d3) or (d3 + 1 == d2 and d3 + 2 == d1) or (d3 + 1 == d1 and d3 - 1 == d2):
    print(d1 + d2 + d3)
elif d1 == d2:
    print(d1 * d2)
elif d1 == d3:
    print(d1 * d3)
elif d2 == d3:
    print(d2 * d3)
else:
    print('Não Deu')
