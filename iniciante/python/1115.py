# -*- coding: utf-8 -*-

while True:
    line = input().split()
    x = int(line[0])
    y = int(line[1])

    if x == 0 or y == 0:
        break
    elif x > 0 and y > 0:
        print('primeiro')
    elif x < 0 < y:
        print('segundo')
    elif x < 0 and y < 0:
        print('terceiro')
    elif x > 0 > y:
        print('quarto')
