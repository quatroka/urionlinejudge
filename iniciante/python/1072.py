# -*- coding: utf-8 -*-

n = int(input())

cont_in = 0
cont_out = 0

for i in range(0, n):
    y = int(input())
    if(y >= 10 and y <= 20):
        cont_in += 1
    else:
        cont_out += 1
print('%s in' % cont_in)
print('%s out' % cont_out)
