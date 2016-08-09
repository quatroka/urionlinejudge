# -*- coding: utf-8 -*-

line = input()
line = line.split()
a = float(line[0])
b = float(line[1])
c = float(line[2])

print('TRIANGULO: %.3f' % ((a * c) / 2))
print('CIRCULO: %.3f' % (c**2 * 3.14159))
print('TRAPEZIO: %.3f' % ((a + b) * c / 2))
print('QUADRADO: %.3f' % (b * b))
print('RETANGULO: %.3f' % (a * b))
