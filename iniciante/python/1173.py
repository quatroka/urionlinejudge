# -*- coding: utf-8 -*-

v = [int(input())]

print('N[0] = %s' % v[0])

for i in range(1, 10):
    v.append(v[i - 1] * 2)
    print('N[%s] = %s' % (i, v[i]))
