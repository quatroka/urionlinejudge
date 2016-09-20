# -*- coding: utf-8 -*-

line = input()
line = line.split()
a = float(line[0])
b = float(line[1])
c = float(line[2])

delta = b**2 - (4 * a * c)

if delta <= 0 or a == 0:
    print('Impossivel calcular')
else:
    r1 = (-b + (delta**(1 / 2))) / (2 * a)
    r2 = (-b - (delta**(1 / 2))) / (2 * a)
    print('R1 = %.5f' % r1)
    print('R2 = %.5f' % r2)
