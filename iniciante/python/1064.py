# -*- coding: utf-8 -*-

cont = 0
media = 0
for i in range(0, 6):
    x = float(input())
    if x > 0:
        media += x
        cont += 1

print('%s valores positivos' % cont)
print('%.1f' % (media / cont))
