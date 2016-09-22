# -*- coding: utf-8 -*-

n = int(input())

menor = 0
posicao = 0
x = input().split()
for i in range(len(x)):
    x[i] = int(x[i])
    if x[i] < menor:
        menor = x[i]
        posicao = i

print('Menor valor: %s' % menor)
print('Posicao: %s' % posicao)
