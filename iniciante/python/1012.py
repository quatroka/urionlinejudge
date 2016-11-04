# -*- coding: utf-8 -*-

line = input()
line = line.split()
a = float(line[0])
b = float(line[1])
c = float(line[2])

print('TRIANGULO: {0:.3f}'.format(((a * c) / 2)))
print('CIRCULO: {0:.3f}'.format((c**2 * 3.14159)))
print('TRAPEZIO: {0:.3f}'.format(((a + b) * c / 2)))
print('QUADRADO: {0:.3f}'.format((b * b)))
print('RETANGULO: {0:.3f}'.format((a * b)))
