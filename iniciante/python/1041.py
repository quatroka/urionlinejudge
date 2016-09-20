# -*- coding: utf-8 -*-

line = input()
line = line.split()

x = float(line[0])
y = float(line[1])

if x == 0 and y == 0:
    print('Origem')

if x == 0 and y != 0:
    print('Eixo Y')

if x != 0 and y == 0:
    print('Eixo X')

if x > 0 and y > 0:
    print('Q1')

if x < 0 < y:
    print('Q2')

if x < 0 and y < 0:
    print('Q3')

if x > 0 > y:
    print('Q4')
