# -*- coding: utf-8 -*-

choice = 1
while choice != 0:
    choice = int(input())
    if choice == 0:
        break
    else:
        for i in range(1, choice + 1):
            if i == choice:
                print('%s' % i)
            else:
                print('%s ' % i, end='')
