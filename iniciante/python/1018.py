# -*- coding: utf-8 -*-

valor = int(input())

print(valor)

print('{0:d} nota(s) de R$ 100,00'.format((valor // 100)))
valor %= 100

print('{0:d} nota(s) de R$ 50,00'.format((valor // 50)))
valor %= 50

print('{0:d} nota(s) de R$ 20,00'.format((valor // 20)))
valor %= 20

print('{0:d} nota(s) de R$ 10,00'.format((valor // 10)))
valor %= 10

print('{0:d} nota(s) de R$ 5,00'.format((valor // 5)))
valor %= 5

print('{0:d} nota(s) de R$ 2,00'.format((valor // 2)))
valor %= 2

print('{0:d} nota(s) de R$ 1,00'.format(valor))
