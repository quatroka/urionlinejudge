# -*- coding: utf-8 -*-

n = int(input())

anos = n // 365
n = n % 365
meses = n // 30
n = n % 30

print('%d ano(s)' % anos)
print('%d mes(es)' % meses)
print('%d dia(s)' % n)
