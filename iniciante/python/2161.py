# -*- coding: utf-8 -*-

n = int(input())

total = 0
for i in range(n, 0, -1):
    total = 1 / (6 + total)

print('%.10f' % (total + 3))
