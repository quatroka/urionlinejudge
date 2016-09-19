# -*- coding: utf-8 -*-

x = int(input())
cont = 0

for i in range(x, (x * 3)):
    if(cont == 6):
        break
    elif(i % 2 == 1):
        print(i)
        cont += 1
