# -*- coding: utf-8 -*-

media = 0
x = 0
while x < 2:
    n = float(input())
    if 0 <= n <= 10:
        media += n
        x += 1
    else:
        print('nota invalida')

print('media = {0!s}'.format((media / 2)))
