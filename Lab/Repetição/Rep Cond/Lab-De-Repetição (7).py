import random

papel = 1
tesoura = 2
pedra = 3
vitoria = 0
derrota = 0

while derrota < 3 and vitoria < 3:
    jogadadoplayer = int(input('qual sua jogada 1-papel 2-tesoura 3-pedra : '))
    jogadadopc = random.randint(1, 3)

    if jogadadoplayer == 3:
        jogadadoplayer = 'pedra'
    if jogadadopc == 3:
        jogadadopc = 'pedra'

    if jogadadoplayer == 2:
        jogadadoplayer = 'tesoura'
    if jogadadopc == 2:
        jogadadopc = 'tesoura'

    if jogadadoplayer == 1:
        jogadadoplayer = 'papel'
    if jogadadopc == 1:
        jogadadopc = 'papel'

    if jogadadoplayer == jogadadopc:
        print(jogadadoplayer, 'empatou')
        print('Vitórias =', vitoria, 'Derrotas =', derrota)

    if jogadadoplayer == 'papel' and jogadadopc == 'pedra':
        print(jogadadoplayer, 'você venceu')
        vitoria = vitoria + 1
        print('Vitórias =', vitoria, 'Derrotas =', derrota)
    if jogadadoplayer == 'tesoura' and jogadadopc == 'papel':
        print(jogadadoplayer, 'você venceu')
        vitoria = vitoria + 1
        print('Vitórias =', vitoria, 'Derrotas =', derrota)
    if jogadadoplayer == 'pedra' and jogadadopc == 'tesoura':
        print(jogadadoplayer, 'você venceu')
        vitoria = vitoria + 1
        print('Vitórias =', vitoria,  'Derrotas =', derrota)

    if jogadadoplayer == 'pedra' and jogadadopc == 'papel':
        print(jogadadoplayer, 'você perdeu')
        derrota = derrota + 1
        print('Vitórias =', vitoria, 'Derrotas =', derrota)
    if jogadadoplayer == 'papel' and jogadadopc == 'tesoura':
        print(jogadadoplayer, 'você perdeu')
        derrota = derrota + 1
        print('Vitórias =', vitoria, 'Derrotas =', derrota)
    if jogadadoplayer == 'tesoura' and jogadadopc == 'pedra':
        print(jogadadoplayer, 'você perdeu')
        derrota = derrota + 1
        print('Vitórias =', vitoria, 'Derrotas =', derrota)

if vitoria == 3:
    print('VITORIA :)')
if derrota == 3:
    print('DERROTA :(')
