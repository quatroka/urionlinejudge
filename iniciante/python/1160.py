# -*- coding: utf-8 -*-

t = int(input())

for i in range(0, t):
    line = input().split()
    pa = int(line[0])
    pb = int(line[1])
    g1 = float(line[2])
    g2 = float(line[3])

    anos = 0
    while pa <= pb:
        pa = int(pa * ((g1 / 100) + 1))
        pb = int(pb * ((g2 / 100) + 1))
        anos += 1
        if anos > 100:
            break

    if anos > 100:
        print('Mais de 1 seculo.')
    else:
        print('{0!s} anos.'.format(anos))
