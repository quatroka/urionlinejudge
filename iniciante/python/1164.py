# -*- coding: utf-8 -*-

cases = int(input())

for i in range(0, cases):
    n = int(input())
    soma = 0

    for j in range(1, n):
        if n % j == 0:
            soma += j

    if soma != n:
        print('{0!s} nao eh perfeito'.format(n))
    else:
        print('{0!s} eh perfeito'.format(n))
