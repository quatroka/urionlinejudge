#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while True:
    try:
        BEST = 0
        HIGH = 0
        for i in range(0, int(input())):
            time, length = input().split()
            SCORE = int(length) / int(time)
            if SCORE > HIGH:
                HIGH = SCORE
                print(i + 1)
    except EOFError:
        break
