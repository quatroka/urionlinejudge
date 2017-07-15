#!/usr/bin/env python3
# -*- coding: utf-8 -*-
for i in range(0, int(input())):
    PLAYERS = input().split()
    NUMS = input().split()
    PAIR = False

    if (int(NUMS[0]) + int(NUMS[1])) % 2 == 0:
        PAIR = True

    if PLAYERS[1] == 'PAR' and PAIR:
        print(PLAYERS[0])
    elif PLAYERS[3] == 'IMPAR' and not PAIR:
        print(PLAYERS[2])
    elif PLAYERS[1] == 'IMPAR' and not PAIR:
        print(PLAYERS[0])
    else:
        print(PLAYERS[2])
