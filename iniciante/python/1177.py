# -*- coding: utf-8 -*-

t = int(input())
v = []

n = 0
for i in range(0, 1000):
    v.append(n)
    n += 1
    if n == t:
        n = 0
    print('N[{0!s}] = {1!s}'.format(i, v[i]))
