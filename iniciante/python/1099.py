# -*- coding: utf-8 -*-

n = int(input())

for i in range(0, n):
    soma = 0
    xy = input().split()
    x = int(xy[0])
    y = int(xy[1])
    if(x < y):
        for j in range(x + 1, y):
            if(j % 2 == 1):
                soma += j
    else:
        for i in range(x - 1, y, -1):
            if(i % 2 == 1):
                soma += i
    print(soma)
