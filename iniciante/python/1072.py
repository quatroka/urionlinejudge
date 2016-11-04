# -*- coding: utf-8 -*-

n = int(input())

cont_in = 0
cont_out = 0

for i in range(0, n):
    y = int(input())
    if 10 <= y <= 20:
        cont_in += 1
    else:
        cont_out += 1
print('{0!s} in'.format(cont_in))
print('{0!s} out'.format(cont_out))
