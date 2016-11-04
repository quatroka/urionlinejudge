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

print('{0!s} valor(es) par(es)'.format(par))
print('{0!s} valor(es) impar(es)'.format(impar))
print('{0!s} valor(es) positivo(s)'.format(positivo))
print('{0!s} valor(es) negativo(s)'.format(negativo))
