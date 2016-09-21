# -*- coding: utf-8 -*-

n = int(input())

for i in range(0, n):
    line = input().split()
    x = int(line[0])
    y = int(line[1])

    soma = 0
    for j in range(0, y * 2):
        if x % 2 == 1:
            soma += x
        x += 1

    print(soma)
