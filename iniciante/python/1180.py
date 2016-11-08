# -*- coding: utf-8 -*-

n = int(input())

menor = 0
posicao = 0
x = input().split()
for i in range(0, len(x)):
    x[i] = int(x[i])
    if x[i] < menor:
        menor = x[i]
        posicao = i

print('Menor valor: {0!s}'.format(menor))
print('Posicao: {0!s}'.format(posicao))
