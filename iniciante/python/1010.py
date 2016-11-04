# -*- coding: utf-8 -*-

p1 = input()
p1 = p1.split()
p2 = input()
p2 = p2.split()
totalp1 = int(p1[1]) * float(p1[2])
totalp2 = int(p2[1]) * float(p2[2])

print('VALOR A PAGAR: R$ {0:.2f}'.format((totalp1 + totalp2)))
