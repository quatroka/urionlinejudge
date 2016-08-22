# -*- coding: utf-8 -*-

while(True):
    soma = 0
    nums = ''
    line = input().split()
    x = int(line[0])
    y = int(line[1])
    if(x <= 0 or y <= 0):
        break
    else:
        if(x > y):
            for i in range(y, x + 1):
                nums += '%s ' % i
                soma += i
        else:
            for i in range(x, y + 1):
                nums += '%s ' % i
                soma += i
        print('%sSum=%s' % (nums, soma))
