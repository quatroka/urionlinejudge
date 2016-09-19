# -*- coding: utf-8 -*-

n = int(input())

for i in range(0, n):
    xy = input().split()
    x = int(xy[0])
    y = int(xy[1])
    if(y == 0):
        print('divisao impossivel')
    else:
        print('%.1f' % float(x / y))
