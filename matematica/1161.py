#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def fat(n):
    """ Calculate fatorial of one number """
    n_fat = 1
    for i in range(2, n + 1):
        n_fat = n_fat * i
    return n_fat
while True:
    try:
        N1, N2 = input().split()
        print(fat(int(N1)) + fat(int(N2)))
    except EOFError:
        break
