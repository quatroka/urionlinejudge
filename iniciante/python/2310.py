#!/usr/bin/env python3
# -*- coding: utf-8 -*-
SBA = [0, 0, 0]
S1B1A1 = [0, 0, 0]
for i in range(0, int(input())):
    NAME = input()
    SBA_I = input().split()
    S1B1A1_I = input().split()
    for j in range(0, 3):
        SBA[j] += int(SBA_I[j])
        S1B1A1[j] += int(S1B1A1_I[j])

print('Pontos de Saque: {0:.2f} %.'.format(S1B1A1[0] * 100 / SBA[0]))
print('Pontos de Bloqueio: {0:.2f} %.'.format(S1B1A1[1] * 100 / SBA[1]))
print('Pontos de Ataque: {0:.2f} %.'.format(S1B1A1[2] * 100 / SBA[2]))
