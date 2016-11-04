# -*- coding: utf-8 -*-

n = []
for i in range(0, 100):
    n.append(float(input()))
    if n[i] <= 10:
        print('A[{0!s}] = {1!s}'.format(i, n[i]))
