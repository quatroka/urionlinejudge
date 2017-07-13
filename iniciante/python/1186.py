#!/usr/bin/env python3
# -*- coding: utf-8 -*-
OP = input()

DATA = []
for i in range(0, 12):
    DATA_AUX = []
    for j in range(0, 12):
        DATA_AUX.append(float(input()))
    DATA.append(DATA_AUX)

RESULT = 0
COUNT = 0
for x in range(1, 12):
    COUNT += x
    for y in range(11, 11 - x, -1):
        RESULT += DATA[x][y]

if OP == 'M':
    print('{0:.1f}'.format(RESULT / COUNT))
else:
    print(RESULT)
