# -*- coding: utf-8 -*-

v = [int(input())]

print('N[0] = {0!s}'.format(v[0]))

for i in range(1, 10):
    v.append(v[i - 1] * 2)
    print('N[{0!s}] = {1!s}'.format(i, v[i]))
