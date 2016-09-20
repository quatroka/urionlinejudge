# -*- coding: utf-8 -*-

cont = 0
for i in range(0, 5):
    x = int(input())
    if x % 2 == 0:
        cont += 1

print('%s valores pares' % cont)
