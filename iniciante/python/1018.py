# -*- coding: utf-8 -*-

valor = int(input())

print(valor)

print('%d nota(s) de R$ 100,00' % (valor // 100))
valor %= 100

print('%d nota(s) de R$ 50,00' % (valor // 50))
valor %= 50

print('%d nota(s) de R$ 20,00' % (valor // 20))
valor %= 20

print('%d nota(s) de R$ 10,00' % (valor // 10))
valor %= 10

print('%d nota(s) de R$ 5,00' % (valor // 5))
valor %= 5

print('%d nota(s) de R$ 2,00' % (valor // 2))
valor %= 2

print('%d nota(s) de R$ 1,00' % valor)
