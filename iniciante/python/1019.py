# -*- coding: utf-8 -*-

n = int(input())

horas = n // 3600
n %= 3600
minutos = n // 60
n %= 60

print('{0:d}:{1:d}:{2:d}'.format(horas, minutos, n))
