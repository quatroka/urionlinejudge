# -*- coding: utf-8 -*-

line = input()
line = line.split()
A = int(line[0])
B = int(line[1])
C = int(line[2])
D = int(line[3])

if(B > C and D > A and (C + D) > (A + B) and
   C > 0 and D > 0 and A % 2 != 1):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
