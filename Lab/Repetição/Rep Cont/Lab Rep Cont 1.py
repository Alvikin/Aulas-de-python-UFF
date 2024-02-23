coroa = 0
jovens = 0
altjovem = 0
magros = 0
pessoas = 0
for x in range(5):

    pessoas = pessoas + 1

    idade = int(input('Idade: '))
    if idade > 50:
        coroa = coroa + 1

    altura = float(input('Altura:'))
    if idade >= 10 and idade <= 20:
        jovens = jovens + 1
        altjovem = altjovem + altura

    peso = float(input('Peso: '))
    if peso < 40:
        magros = magros + 1

if coroa == 0:
    print('Não houveram coroas')
else:
    print('Coroas = ', coroa)

if altjovem == 0:
    print('Não houveram jovens')
else:
    print('Média de alturas dos jovens = ', altjovem / jovens)

if magros == 0:
    print('Não houveram magros')
else:
    print('Magros = ', ((magros / pessoas) * 100), '%')
