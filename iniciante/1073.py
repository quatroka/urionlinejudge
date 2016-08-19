# -*- coding: utf-8 -*-

n = int(input())

for i in range(1, n + 1):
    if(i % 2 == 0):
        print('%s^2 = %s' % (i, i**2))
