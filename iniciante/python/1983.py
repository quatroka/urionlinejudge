# -*- coding: utf-8 -*-

tests = int(input())

maior_nota = 0
melhor_aluno = 0
for i in range(0, tests):
    line = input().split()
    aluno = int(line[0])
    nota = float(line[1])

    if nota > maior_nota:
        maior_nota = nota
        melhor_aluno = aluno


if maior_nota < 8:
    print('Minimum note not reached')
else:
    print(melhor_aluno)
