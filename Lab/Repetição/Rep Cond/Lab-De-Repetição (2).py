n      = int(input("Digite um número inteiro positivo: "))
numero = 2
primo  = True
while numero < n:
    if (n % numero ==0):
        print(numero)
        primo = False
    numero = numero + 1

if (primo):
    print('É primo')
else:
    print('Não é primo')
