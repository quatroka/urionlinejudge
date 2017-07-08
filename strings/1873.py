#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())

for i in range(0, N):
    rajesh, sheldon = input().split()
    table = {
        'lagarto': ['papel', 'spock'],
        'papel': ['pedra', 'spock'],
        'pedra': ['lagarto', 'tesoura'],
        'spock': ['pedra', 'tesoura'],
        'tesoura': ['lagarto', 'papel']
    }

    if rajesh == sheldon:
        print('empate')
    elif table[rajesh][0] == sheldon or table[rajesh][1] == sheldon:
        print('rajesh')
    else:
        print('sheldon')
