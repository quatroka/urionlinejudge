# -*- coding: utf-8 -*-

x = int(input())
while x != 0:

    soma = 0
    for j in range(0, 10):
        if x % 2 == 0:
            soma += x
        x += 1

    print(soma)
    x = int(input())
