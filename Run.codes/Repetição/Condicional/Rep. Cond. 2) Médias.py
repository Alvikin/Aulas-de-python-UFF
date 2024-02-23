alunos = int(input())
alunoslimite = 1
mediatotal = 0
while alunoslimite <= alunos:
    nota1 = float(input())
    nota2 = float(input())
    media = (nota1 + nota2) / 2
    mediatotal = mediatotal + media
    alunoslimite = alunoslimite + 1
print('%.2f' % mediatotal)
