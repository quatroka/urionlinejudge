#!/usr/bin/env python3
# -*- coding: utf-8 -*-
qtd = int(input())

soma = 0
for i in range(0, qtd):
    line = input().split()
    item = line[0]
    qtd_item = int(line[1])

    if item == '1001':
        soma += 1.5 * qtd_item
    elif item == '1002':
        soma += 2.5 * qtd_item
    elif item == '1003':
        soma += 3.5 * qtd_item
    elif item == '1004':
        soma += 4.5 * qtd_item
    elif item == '1005':
        soma += 5.5 * qtd_item

print('{0:.2f}'.format(soma))
