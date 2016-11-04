# -*- coding: utf-8 -*-

media = 0
cont = 0

while True:
    n = int(input())

    if n < 0:
        break
    else:
        cont += 1
        media += n

print('{0:.2f}'.format((media / cont)))
