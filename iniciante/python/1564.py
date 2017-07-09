#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while True:
    try:
        N = int(input())
        if N < 1:
            print('vai ter copa!')
        else:
            print('vai ter duas!')
    except EOFError:
        break
