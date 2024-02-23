SB = int(input('Digite salário bruto: '))
if SB < 500:
    print(SB)
elif SB >= 500 and SB < 800:
    print(SB * 0.9)
elif SB >= 800 and SB < 1000:
    print(SB * 0.85)
elif SB >= 1000:
    print(SB * 0.2)
