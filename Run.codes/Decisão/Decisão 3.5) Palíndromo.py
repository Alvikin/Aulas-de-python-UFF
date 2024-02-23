numero = int(input())
algaritmo1 = numero // 10000
algaritmo2 = numero // 1000 % 10
algaritmo3 = numero // 100 % 10
algaritmo4 = numero // 10 % 10
algaritmo5 = numero % 10
if algaritmo1 == algaritmo5 and algaritmo2 == algaritmo4:
    print('sim')
else:
    print('não')
