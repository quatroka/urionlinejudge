# -*- coding: utf-8 -*-

valores = input()
valores = valores.split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

maior_A_B = (a + b + abs(a - b)) / 2
maior_A_B_C = (maior_A_B + c + abs(maior_A_B - c)) / 2

print('{0:d} eh o maior'.format(maior_A_B_C))
