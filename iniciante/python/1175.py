# -*- coding: utf-8 -*-

n = []
for i in range(0, 20):
    n.append(int(input()))

for j in range(0, 10):
    n[j], n[19 - j] = n[19 - j], n[j]

for k in range(0, 20):
    print('N[%s] = %s' % (k, n[k]))
