videogames = [0] * 10
gratis = []

for i in range(10):
   videogames[i] = int(input())

for j in range(10):
    videogames[j] = videogames[j] // 5

print(videogames)