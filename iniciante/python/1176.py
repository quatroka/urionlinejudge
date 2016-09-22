# -*- coding: utf-8 -*-

n1 = 0
n2 = 1
seq_fibo = []
for i in range(0, 61):
    seq_fibo.append(n1)
    n1, n2 = n2, n1 + n2

t = int(input())
for j in range(0, t):
    n = int(input())
    print('Fib(%s) = %s' % (n, seq_fibo[n]))
