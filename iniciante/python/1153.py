# -*- coding: utf-8 -*-

n = int(input())

total = 1
for i in range(n, 0, -1):
    total *= i

print(total)
