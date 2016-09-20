# -*- coding: utf-8 -*-

n = float(input())

if 0 <= n <= 25:
    print('Intervalo [0,25]')
if 25 < n <= 50:
    print('Intervalo (25,50]')
if 50 < n <= 75:
    print('Intervalo (50,75]')
if 75 < n <= 100:
    print('Intervalo (75,100]')
if n < 0 or n > 100:
    print('Fora de intervalo')
