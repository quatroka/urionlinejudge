# -*- coding: utf-8 -*-

n = int(input())
n1 = 0
n2 = 1

for i in range(0, n):
    if n - 1 == i:
        print('%s' % n1)
    else:
        print('%s ' % n1, end='')
    n1, n2 = n2, n1 + n2
