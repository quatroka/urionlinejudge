# -*- coding: utf-8 -*-

n = int(input())
total = 0
total_c = 0
total_r = 0
total_s = 0

for i in range(0, n):
    cobaia = input().split()
    qtd = int(cobaia[0])
    tipo = cobaia[1]
    if(tipo == 'C'):
        total_c += qtd
    elif(tipo == 'R'):
        total_r += qtd
    elif(tipo == 'S'):
        total_s += qtd

total = total_c + total_r + total_s
print('Total: %s cobaias' % total)
print('Total de coelhos: %s' % total_c)
print('Total de ratos: %s' % total_r)
print('Total de sapos: %s' % total_s)
print('Percentual de coelhos: %.2f %%' % (total_c * 100 / total))
print('Percentual de ratos: %.2f %%' % (total_r * 100 / total))
print('Percentual de sapos: %.2f %%' % (total_s * 100 / total))
