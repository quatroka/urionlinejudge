# -*- coding: utf-8 -*-

line = input().split()

ini_h = int(line[0])
ini_m = int(line[1])
fim_h = int(line[2])
fim_m = int(line[3])

h = fim_h - ini_h
m = fim_m - ini_m

if h < 0:
    h += 24

if m < 0:
    m += 60
    h -= 1

if ini_h == fim_h and ini_m == fim_m:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif ini_h == fim_h and ini_m > fim_m:
    print('O JOGO DUROU %s HORA(S) E %s MINUTO(S)' % (h + 24, m))
else:
    print('O JOGO DUROU %s HORA(S) E %s MINUTO(S)' % (h, m))
