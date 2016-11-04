# -*- coding: utf-8 -*-

n = int(input())

total = 0
for i in range(n, 0, -1):
    total = 1 / (2 + total)

print('{0:.10f}'.format((total + 1)))
