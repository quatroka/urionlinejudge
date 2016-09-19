# -*- coding: utf-8 -*-

media = 0
x = 0
while(x < 2):
    n = float(input())
    if(n < 0 or n > 10):
        print('nota invalida')
    else:
        media += n
        x += 1

print('media = %s' % (media / 2))
