#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = input().split()
SUMS = 0
for i in range(0, len(N)):
    SUMS += int(N[i])
print(SUMS - 3)
