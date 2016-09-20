# -*- coding: utf-8 -*-

posicao = 0
maior = 0
for i in range(1, 101):
    n = int(input())
    if n > maior:
        maior = n
        posicao = i

print(maior)
print(posicao)
