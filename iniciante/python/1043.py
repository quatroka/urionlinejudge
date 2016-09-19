# -*- coding: utf-8 -*-

# Para verificar se as medidas formam um trianulo dados os
# lados a, b e c; e preencha o seguinte requesito: um lado
# tem que ser menor que a soma dos outros dois. Logo:
# a < b + c; b < a + c; c < a + b.

line = input().split()
a = float(line[0])
b = float(line[1])
c = float(line[2])

if(a < (b + c) and b < (a + c) and c < (a + b)):
    print('Perimetro = %.1f' % (a + b + c))
else:
    print('Area = %.1f' % (((a + b) * c) / 2))
