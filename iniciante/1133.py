# -*- coding: utf-8 -*-

x = int(input())
y = int(input())

if(x != y):
    if(x > y):
        aux = x
        x = y
        y = aux

    for i in range(x + 1, y):
        if(i % 5 == 2 or i % 5 == 3):
            print(i)
