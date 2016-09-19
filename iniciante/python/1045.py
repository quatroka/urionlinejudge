# -*- coding: utf-8 -*-

line = input().split()

c = float(line[0])
b = float(line[1])
a = float(line[2])

if(a < b):
    temp = a
    a = b
    b = temp
if(b < c):
    temp = b
    b = c
    c = temp
if(a < b):
    temp = a
    a = b
    b = temp


if(a >= b + c):
    print('NAO FORMA TRIANGULO')
else:
    if(a**2 == (b**2) + (c**2)):
        print('TRIANGULO RETANGULO')

    if((a**2) > (b**2) + (c**2)):
        print('TRIANGULO OBTUSANGULO')

    if((a**2) < (b**2) + (c**2)):
        print('TRIANGULO ACUTANGULO')

    if(a == b and b == c):
        print('TRIANGULO EQUILATERO')

    if((a == b and a != c and b != c) or
       (a != b and a == c and b != c) or
       (a != b and a != c and b == c)):
        print('TRIANGULO ISOSCELES')
