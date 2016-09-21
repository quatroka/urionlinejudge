# -*- coding: utf-8 -*-

s = 1
for i in range(1, 20):
    s += (i * 2 + 1) / (2**i)

print('%.2f' % s)
