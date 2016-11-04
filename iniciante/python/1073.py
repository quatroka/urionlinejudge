# -*- coding: utf-8 -*-

n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        print('{0!s}^2 = {1!s}'.format(i, i**2))
