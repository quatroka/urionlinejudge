# -*- coding: utf-8 -*-

n = int(input())
total_c = 0
total_r = 0
total_s = 0

for i in range(0, n):
    cobaia = input().split()
    qtd = int(cobaia[0])
    tipo = cobaia[1]
    if tipo == 'C':
        total_c += qtd
    elif tipo == 'R':
        total_r += qtd
    elif tipo == 'S':
        total_s += qtd

total = total_c + total_r + total_s
print('Total: {0!s} cobaias'.format(total))
print('Total de coelhos: {0!s}'.format(total_c))
print('Total de ratos: {0!s}'.format(total_r))
print('Total de sapos: {0!s}'.format(total_s))
print('Percentual de coelhos: {0:.2f} %'.format((total_c * 100 / total)))
print('Percentual de ratos: {0:.2f} %'.format((total_r * 100 / total)))
print('Percentual de sapos: {0:.2f} %'.format((total_s * 100 / total)))
