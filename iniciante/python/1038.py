# -*- coding: utf-8 -*-

line = input()
line = line.split()

item = int(line[0])
qtd = int(line[1])

if item == 1:
    print('Total: R$ {0:.2f}'.format((qtd * 4)))
if item == 2:
    print('Total: R$ {0:.2f}'.format((qtd * 4.5)))
if item == 3:
    print('Total: R$ {0:.2f}'.format((qtd * 5)))
if item == 4:
    print('Total: R$ {0:.2f}'.format((qtd * 2)))
if item == 5:
    print('Total: R$ {0:.2f}'.format((qtd * 1.5)))
