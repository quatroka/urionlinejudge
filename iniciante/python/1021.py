# -*- coding: utf-8 -*-

valor = float(input())

n100 = valor // 100
valor %= 100
n50 = valor // 50
valor %= 50
n20 = valor // 20
valor %= 20
n10 = valor // 10
valor %= 10
n5 = valor // 5
valor %= 5
n2 = valor // 2
valor %= 2

m1 = valor // 1
valor = (valor % 1) * 100
m50 = valor // 50
valor %= 50
m25 = valor // 25
valor %= 25
m10 = valor // 10
valor %= 10
m5 = valor // 5
valor %= 5

print('NOTAS:')
print('{0:d} nota(s) de R$ 100.00'.format(n100))
print('{0:d} nota(s) de R$ 50.00'.format(n50))
print('{0:d} nota(s) de R$ 20.00'.format(n20))
print('{0:d} nota(s) de R$ 10.00'.format(n10))
print('{0:d} nota(s) de R$ 5.00'.format(n5))
print('{0:d} nota(s) de R$ 2.00'.format(n2))
print('MOEDAS:')
print('{0:d} moeda(s) de R$ 1.00'.format(m1))
print('{0:d} moeda(s) de R$ 0.50'.format(m50))
print('{0:d} moeda(s) de R$ 0.25'.format(m25))
print('{0:d} moeda(s) de R$ 0.10'.format(m10))
print('{0:d} moeda(s) de R$ 0.05'.format(m5))
print('{0:d} moeda(s) de R$ 0.01'.format(valor))
