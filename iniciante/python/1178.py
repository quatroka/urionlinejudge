# -*- coding: utf-8 -*-

x = float(input())

v = []
for i in range(0, 100):
    v.append(x)
    print('N[%s] = %.4f' % (i, v[i]))
    x /= 2
