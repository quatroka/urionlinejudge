# -*- coding: utf-8 -*-

valores = input()
valores = valores.split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

maior_ab = (a + b + abs(a - b)) / 2
maior_abc = (maior_ab + c + abs(maior_ab - c)) / 2

print('{0:d} eh o maior'.format(maior_abc))
