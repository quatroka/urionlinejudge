# -*- coding: utf-8 -*-

n = int(input())

horas = n // 3600
n = n % 3600
minutos = n // 60
n = n % 60

print('%d:%d:%d' % (horas, minutos, n))
