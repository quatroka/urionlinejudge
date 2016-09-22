# -*- coding: utf-8 -*-

pares = []
impares = []

for i in range(0, 15):
    n = int(input())

    if n % 2 == 0:
        if len(pares) == 5:
            for j in range(0, 5):
                print('par[%s] = %s' % (j, pares[j]))
            del pares[:]
        pares.append(n)
    else:
        if len(impares) == 5:
            for k in range(0, 5):
                print('impar[%s] = %s' % (k, impares[k]))
            del impares[:]
        impares.append(n)

for m in range(0, len(impares)):
    print('impar[%s] = %s' % (m, impares[m]))

for l in range(0, len(pares)):
    print('par[%s] = %s' % (l, pares[l]))
