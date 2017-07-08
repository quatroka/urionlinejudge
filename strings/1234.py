#!/usr/bin/env python3
# -*- coding: utf-8
while True:
    try:
        UPPER = False
        STRING = list(input())

        for i in range(0, len(STRING)):
            if STRING[i] != ' ':
                if UPPER is False:
                    STRING[i] = STRING[i].upper()
                    UPPER = True
                else:
                    STRING[i] = STRING[i].lower()
                    UPPER = False

        print(''.join(STRING))
    except EOFError:
        break
