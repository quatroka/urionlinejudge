#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = input()
TEAS = input().split()
SUM = 0
for tea in TEAS:
    if N == tea:
        SUM += 1
print(SUM)
