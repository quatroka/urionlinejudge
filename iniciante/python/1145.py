# -*- coding: utf-8 -*-

line = input().split()
x = int(line[0])
y = int(line[1])

count = 0
for i in range(1, y + 1):
    count += 1
    if count == x:
        print('%s' % i)
        count = 0
    else:
        print('%s ' % i, end='')
