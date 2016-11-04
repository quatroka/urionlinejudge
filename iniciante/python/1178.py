# -*- coding: utf-8 -*-

x = float(input())

v = []
for i in range(0, 100):
    v.append(x)
    print('N[{0!s}] = {1:.4f}'.format(i, v[i]))
    x /= 2
