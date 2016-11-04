# -*- coding: utf-8 -*-

x = []
for i in range(0, 10):
    x.append(int(input()))
    if x[i] <= 0:
        x[i] = 1
    print('X[{0!s}] = {1!s}'.format(i, x[i]))
