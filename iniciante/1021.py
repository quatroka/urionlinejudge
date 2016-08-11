# -*- coding: utf-8 -*-

valor = float(input())

n100 = valor // 100
valor = valor % 100
n50 = valor // 50
valor = valor % 50
n20 = valor // 20
valor = valor % 20
n10 = valor // 10
valor = valor % 10
n5 = valor // 5
valor = valor % 5
n2 = valor // 2
valor = valor % 2

m1 = valor // 1
valor = (valor % 1) * 100
m50 = valor // 50
valor = valor % 50
m25 = valor // 25
valor = valor % 25
m10 = valor // 10
valor = valor % 10
m5 = valor // 5
valor = valor % 5

print('NOTAS:')
print('%d nota(s) de R$ 100.00' % n100)
print('%d nota(s) de R$ 50.00' % n50)
print('%d nota(s) de R$ 20.00' % n20)
print('%d nota(s) de R$ 10.00' % n10)
print('%d nota(s) de R$ 5.00' % n5)
print('%d nota(s) de R$ 2.00' % n2)
print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' % m1)
print('%d moeda(s) de R$ 0.50' % m50)
print('%d moeda(s) de R$ 0.25' % m25)
print('%d moeda(s) de R$ 0.10' % m10)
print('%d moeda(s) de R$ 0.05' % m5)
print('%d moeda(s) de R$ 0.01' % valor)
