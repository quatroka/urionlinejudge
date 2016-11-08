#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())

v = input().split()

test = 0
for i in range(1, len(v)):
    if test != 0:
        break
    elif int(v[i]) < int(v[i - 1]):
        test = i + 1

print(test)
