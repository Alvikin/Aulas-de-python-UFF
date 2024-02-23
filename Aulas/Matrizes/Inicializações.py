#indireta de zeros

turma = []
for i in range(4):               # para cada linha
    linha = []                   # cria linhas vazias
    for j in range(3):           # adiciona colunas nas linhas
        linha.append(0)
    turma.append(linha)          # adiciona linhas na matriz

#         OU

turma = []
for i in range(4):               # para cada linha
    linha = [0] * 3              # cria linhas vazias
    turma.append(linha)          # adiciona linhas na matriz

#         OU

turma = []
for i in range(4):               # para cada linha
    turma.append([0] * 3)        # adiciona linhas na matriz