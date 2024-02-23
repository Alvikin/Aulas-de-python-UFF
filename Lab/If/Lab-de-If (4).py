import random
import math

time1 = input('Nome do primeiro time: ')
time2 = input('Nome do segundo time: ')
time3 = input('Nome do terceiro time: ')
time4 = input('Nome do quarto time: ')
media1 = float(input('Média do time 1: '))
media2 = float(input('Média do time 2: '))
media3 = float(input('Média do time 3: '))
media4 = float(input('Média do time 4: '))
print("-------Semifinal 1-------")
pontuacao1 = random.randint(0, math.ceil(media1))
pontuacao2 = random.randint(0, math.ceil(media2))
pontuacao3 = random.randint(0, math.ceil(media3))
pontuacao4 = random.randint(0, math.ceil(media4))
print(time1, pontuacao1, 'x', pontuacao2, time2)
if pontuacao1 >= pontuacao2:
    print(time1, 'se classificou !')
    classificado1 = time1
    pontuacao1 = random.randint(0, math.ceil(media1))
else:
    print(time2, 'se classificou !')
    classificado1 = time2
    pontuacao1 = random.randint(0, math.ceil(media2))
print("-------Semifinal 2-------")
print(time3, pontuacao3, 'x', pontuacao4, time4)
if pontuacao3 >= pontuacao4:
    print(time3, 'se classificou !')
    classificado2 = time3
    pontuacao2 = random.randint(0, math.ceil(media3))
else:
    print(time4, 'se classificou !')
    classificado2 = time4
    pontuacao2 = random.randint(0, math.ceil(media4))
print("-------Final !!!!!!-------")
print(classificado1, pontuacao1, 'x', pontuacao2, classificado2)
if pontuacao1 > pontuacao2:
    print(classificado1, 'GANHOU !!!!!!!!!!!!!!!!!!!!')
elif pontuacao2 > pontuacao1:
    print(classificado2, 'GANHOU !!!!!!!!!!!!!!!!!!!!')
else:
    print('Penalidades')
    penal1 = random.randint(0, 5)
    penal2 = random.randint(0, 5)
    print(classificado1, penal1, 'x', penal2, classificado2)
    if penal1 > penal2:
        print(classificado1, 'GANHOU !!!!!!!!!!!!!!!!!!!!')
    elif penal2 > penal1:
        print(classificado2, 'GANHOU !!!!!!!!!!!!!!!!!!!!')
    else:
        print('Moeda !!!')
        moeda = random.randint(1, 2)
        if moeda == 1:
            print('Deu cara', classificado1, 'GANHOU !!!!!!!!!!!!!!!!!!!!')
        if moeda == 2:
            print('Deu coroa', classificado2, 'GANHOU !!!!!!!!!!!!!!!!!!!!')
