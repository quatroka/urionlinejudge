#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while True:
    try:
        STEPS = int(input())
        H, C, L = input().split()
        MINOR_SIDE = (int(H)**2 + int(C)**2) ** (1 / 2)
        AREA = int(L) * MINOR_SIDE
        print('{0:.4f}'.format(AREA * STEPS / 10000))
    except EOFError:
        break
