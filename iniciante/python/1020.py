# -*- coding: utf-8 -*-

n = int(input())

anos = n // 365
n %= 365
meses = n // 30
n %= 30

print('{0:d} ano(s)'.format(anos))
print('{0:d} mes(es)'.format(meses))
print('{0:d} dia(s)'.format(n))
