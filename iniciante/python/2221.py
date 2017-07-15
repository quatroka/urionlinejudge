#!/usr/bin/env python3
# -*- coding: utf-8 -*-
for i in range(0, int(input())):
    BONUS = int(input())
    A1, D1, L1 = input().split()
    A2, D2, L2 = input().split()

    G1 = ((int(A1) + int(D1)) / 2)
    G2 = ((int(A2) + int(D2)) / 2)
    if int(L1) % 2 == 0:
        G1 += BONUS
    if int(L2) % 2 == 0:
        G2 += BONUS
    if G1 == G2:
        print('Emapate')
    elif G1 > G2:
        print('Dabriel')
    else:
        print('Guarte')
