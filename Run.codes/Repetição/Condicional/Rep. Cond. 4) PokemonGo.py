import math

pokemondea = int(input())
pokemondeb = int(input())
anos = 0
while pokemondea <= pokemondeb:
    pokemondea = math.floor(pokemondea * 1.5)
    pokemondeb = math.floor(pokemondeb * 1.3)
    anos = (anos + 1)
print(int(anos))
