# -*- coding: utf-8 -*-

pares = []
impares = []

for i in range(0, 15):
    n = int(input())

    if n % 2 == 0:
        if len(pares) == 5:
            for j in range(0, 5):
                print('par[{0!s}] = {1!s}'.format(j, pares[j]))
            del pares[:]
        pares.append(n)
    else:
        if len(impares) == 5:
            for k in range(0, 5):
                print('impar[{0!s}] = {1!s}'.format(k, impares[k]))
            del impares[:]
        impares.append(n)

for m in range(0, len(impares)):
    print('impar[{0!s}] = {1!s}'.format(m, impares[m]))

for l in range(0, len(pares)):
    print('par[{0!s}] = {1!s}'.format(l, pares[l]))
