centavos = int(input())
moedade50c = (centavos % 100)
moedade25c = (centavos % 100) % 50
moedade1c = (centavos % 100) % 25
if centavos >= 100:
    print(centavos // 100, ' de 1r')
if 50 <= moedade50c < 100:
        print(moedade50c // 50, ' de 50c')
if 25 <= moedade25c < 50:
            print(moedade25c // 25, ' de 25c')
if 1 <= moedade1c < 25:
                print(moedade1c // 1, ' de 1c')
