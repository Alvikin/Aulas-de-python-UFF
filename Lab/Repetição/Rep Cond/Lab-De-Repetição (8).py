import random

jogo = True
jogadas = 0

while jogo:
    if jogadas == 0:
         jogadadoplayer = str(input('Quer jogar, S ou N ? '))

         if jogadadoplayer == 'N' or jogadadoplayer == 'n':
             print('Okay, tchau o/')
             jogo = False

         if jogadadoplayer == 'S' or jogadadoplayer == 's':
             dados = random.randint(2, 12)
             print('dados =', dados)
             if dados == 11 or dados == 7:
                 print('Você é um natural ! GANHOU')
                 jogo = False

             if dados == 2 or dados == 3 or dados == 12:
                 print('Craps ! Perdeu')
                 jogo = False

             else:
                 print('Seu ponto é', dados)
                 jogadas = jogadas + 1

    if jogadas >= 1:
         jogadadoplayer = str(input('Quer tentar de novo, S ou N ? '))

         if jogadadoplayer == 'N' or jogadadoplayer == 'n':
             print('Okay, tchau o/')
             jogo = False

         if jogadadoplayer == 'S' or jogadadoplayer == 's':
             dados2 = random.randint(1, 12)
             print('dados =', dados2)
             if dados == dados2:
                 print(dados2, 'Você venceu !')
                 jogo = False

             if dados2 == 7:
                 print(dados2, 'Você perdeu :(')
                 jogo = False
