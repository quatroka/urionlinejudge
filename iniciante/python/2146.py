#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
while N != 'EOF':
    print(N - 1)
    if N == 9999:
        break
    N = int(input())
