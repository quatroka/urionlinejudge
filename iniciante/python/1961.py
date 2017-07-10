#!/usr/bin/env python3
# -*- coding: utf-8 -*-
JUMP, TUBES_QTD = input().split()
TUBES = input().split()
for i in range(0, int(TUBES_QTD) - 1):
    if abs(int(TUBES[i]) - int(TUBES[i + 1])) > int(JUMP):
        print('GAME OVER')
        break
    elif i == (int(TUBES_QTD) - 2):
        print('YOU WIN')
