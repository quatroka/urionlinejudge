# -*- coding: utf-8 -*-

salario = float(input())
imposto = 0

if salario <= 2000:
    print('Isento')
else:
    salario -= 2000

    if salario >= 1000:
        imposto += 1000 * 0.08
        salario -= 1000
    else:
        imposto += salario * 0.08
        salario -= salario

    if salario >= 1500:
        imposto += 1500 * 0.18
    else:
        imposto += salario * 0.18
        salario -= salario

    salario -= 1500

    if salario > 0:
        imposto += salario * 0.28

    print('R$ %.2f' % imposto)
