import random

palpite = int(input('Advinhe meu número entre 1 e 10: '))
numero = random.randint(1, 10)
tentativas = 1
erro = True
while erro:
    if palpite != numero:
        tentativas = tentativas + 1
        if palpite < numero:
            print(palpite, 'está abaixo')
        if palpite > numero:
            print(palpite, 'está acima')
        palpite = int(input('Tente novamente: '))
        if palpite == numero:
            erro = False
            print('Ótimo, você acertou o numero', numero, 'em', tentativas, 'tentativas !')
