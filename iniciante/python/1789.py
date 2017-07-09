#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while True:
    try:
        QTD = input()
        MAX_V = max(map(int, input().split()))
        if MAX_V < 10:
            print(1)
        elif MAX_V < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        break
