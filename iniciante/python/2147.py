# -*- coding: utf-8 -*-

tests = int(input())

for i in range(0, tests):
    text = input()
    print('{0:.2f}'.format((len(text) / 100)))
