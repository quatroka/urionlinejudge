# -*- coding: utf-8 -*-

line = input().split()

ini = int(line[0])
fim = int(line[1])

if(ini >= fim):
    print('O JOGO DUROU %s HORA(S)' % ((24 - ini) + fim))
else:
    print('O JOGO DUROU %s HORA(S)' % (fim - ini))
