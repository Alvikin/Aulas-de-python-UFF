x = int(input())
media = 0
soma = 0
produto = 1

n = int(input())
media = media + n
soma = soma + n
produto = produto * n
menor = n
maior = n

for i in range(x - 1):
    n = int(input())
    if 0 <= n and n <= 100:
        media = media + n
        soma = soma + n
        produto = produto * n
        if n <= menor:
           menor = n
        if n >= maior:
           maior = n

print('%.2f' % (media / x))
print(soma)
print(produto)
print(menor)
print(maior)
