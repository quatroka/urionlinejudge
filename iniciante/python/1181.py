# -*- coding: utf-8 -*-

line = int(input())
operation = input()

matriz = []

for i in range(0, 12):
    matriz_aux = []

    for j in range(0, 12):
        matriz_aux.append(float(input()))

    matriz.append(matriz_aux)

soma = 0
for item in matriz[line]:
    soma += item

if operation == 'S':
    print('%.1f' % soma)
else:
    print('%.1f' % (soma / 12))
