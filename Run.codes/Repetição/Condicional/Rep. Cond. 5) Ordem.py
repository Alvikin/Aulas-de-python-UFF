N = int(input())
numeroslidos = 2
crescente = True
numero = int(input())
numerosalvo = numero

while numeroslidos <= N:

    numeroslidos = numeroslidos + 1
    numero = int(input())
    if numero < numerosalvo:
        crescente = False
    numerosalvo = numero

if crescente == False:
    print('não')
if crescente == True:
    print('sim')
