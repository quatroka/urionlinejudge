# -*- coding: utf-8 -*-

salario = float(input())

reajuste = 0
perc = ''

if(salario <= 400):
    reajuste = salario * 0.15
    salario = salario + reajuste
    perc = '15 %'
elif(salario <= 800):
    reajuste = salario * 0.12
    salario = salario + reajuste
    perc = '12 %'
elif(salario <= 1200):
    reajuste = salario * 0.1
    salario = salario + reajuste
    perc = '10 %'
elif(salario <= 2000):
    reajuste = salario * 0.07
    salario = salario + reajuste
    perc = '7 %'
elif(salario > 2000):
    reajuste = salario * 0.04
    salario = salario + reajuste
    perc = '4 %'

print('Novo salario: %.2f' % salario)
print('Reajuste ganho: %.2f' % reajuste)
print('Em percentual: %s' % perc)
