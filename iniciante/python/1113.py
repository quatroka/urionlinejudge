# -*- coding: utf-8 -*-

while True:
    line = input().split()
    x = int(line[0])
    y = int(line[1])
    if x == y:
        break
    elif x < y:
        print('Crescente')
    elif x > y:
        print('Decrescente')
