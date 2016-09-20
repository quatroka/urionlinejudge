# -*- coding: utf-8 -*-

par = 0
impar = 0
positivo = 0
negativo = 0
for i in range(0, 5):
    x = int(input())
    if x % 2 == 0:
        par += 1
    if x % 2 == 1:
        impar += 1
    if x > 0:
        positivo += 1
    if x < 0:
        negativo += 1

print('%s valor(es) par(es)' % par)
print('%s valor(es) impar(es)' % impar)
print('%s valor(es) positivo(s)' % positivo)
print('%s valor(es) negativo(s)' % negativo)
