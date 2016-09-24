# -*- coding: utf-8 -*-

column = int(input())
operation = input()

matriz = []

for i in range(0, 12):
    matriz_aux = []

    for j in range(0, 12):
        matriz_aux.append(float(input()))

    matriz.append(matriz_aux)

soma = 0
for item in matriz:
    soma += item[column]

if operation == 'S':
    print('%.1f' % soma)
else:
    print('%.1f' % (soma / 12))
