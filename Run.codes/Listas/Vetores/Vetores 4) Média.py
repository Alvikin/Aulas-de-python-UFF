l = []
media = 0
prox = 0
result = 0

for i in range(5):
   l.append(float(input()))

for i in range(5):
    media = media + l[i]
media = media / 5

if l[0] >= media:
    prox = l[0] - media

if l[0] < media:
    prox = media - l[0]

for i in range(5):
    if l[i] > media:
        if prox >= l[i] - media:
           prox = l[i] - media

    if l[i] <= media:
        if prox >= media - l[i]:
            prox = media - l[i]

for i in range(5):
    result = media - prox
    if result == l[i]:
        print('%.2f' % result)
        break
