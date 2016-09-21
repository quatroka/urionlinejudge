# -*- coding: utf-8 -*-

x = int(input())
z = int(input())
while x >= z:
    z = int(input())

soma = x
cont = 1
while True:
    soma += x + cont
    cont += 1
    if soma > z:
        break

print(cont)
