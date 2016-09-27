# -*- coding: utf-8 -*-

tests = int(input())

for i in range(0, tests):
    n = input()

    if n[0: 4] == 'Thor':
        print('Y')
    else:
        print('N')