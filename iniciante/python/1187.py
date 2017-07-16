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
for x in range(0, 5):
    COUNT += 12 - ((x + 1) * 2)
    for y in range(x + 1, 11 - x):
        RESULT += DATA[x][y]

if OP == 'M':
    print('{0:.1f}'.format(float(RESULT / 30.0)))
else:
    print('{0:.1f}'.format(float(RESULT)))
