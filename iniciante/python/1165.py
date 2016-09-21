# -*- coding: utf-8 -*-

cases = int(input())

for i in range(0, cases):
    n = int(input())

    primo = True
    for j in range(2, n):
        if n % j == 0:
            primo = False
            break

    if primo == False:
        print('%s nao eh primo' % n)
    else:
        print('%s eh primo' % n)
