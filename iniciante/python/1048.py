# -*- coding: utf-8 -*-

salario = float(input())

reajuste = 0
perc = ''

if salario <= 400:
    reajuste = salario * 0.15
    salario += reajuste
    perc = '15 %'
elif salario <= 800:
    reajuste = salario * 0.12
    salario += reajuste
    perc = '12 %'
elif salario <= 1200:
    reajuste = salario * 0.1
    salario += reajuste
    perc = '10 %'
elif salario <= 2000:
    reajuste = salario * 0.07
    salario += reajuste
    perc = '7 %'
elif salario > 2000:
    reajuste = salario * 0.04
    salario += reajuste
    perc = '4 %'

print('Novo salario: {0:.2f}'.format(salario))
print('Reajuste ganho: {0:.2f}'.format(reajuste))
print('Em percentual: {0!s}'.format(perc))
