# -*- coding: utf-8 -*-

p1 = input()
p1 = p1.split()
p2 = input()
p2 = p2.split()
x1 = float(p1[0])
y1 = float(p1[1])
x2 = float(p2[0])
y2 = float(p2[1])

dist = ((x2 - x1)**2 + (y2 - y1)**2)**(1 / 2)
print('%.4f' % dist)
