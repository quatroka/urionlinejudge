# -*- coding: utf-8 -*-

n = int(input())

for i in range(0, n):
    line = input().split()
    a = float(line[0])
    b = float(line[1])
    c = float(line[2])

    media = (a * 2 + b * 3 + c * 5) / 10

    print('%.1f' % media)
