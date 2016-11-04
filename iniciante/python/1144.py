# -*- coding: utf-8 -*-

n = int(input())

for i in range(1, n + 1):
    print('{0!s} {1!s} {2!s}'.format(i, i**2, i**3))
    print('{0!s} {1!s} {2!s}'.format(i, i**2 + 1, i**3 + 1))
