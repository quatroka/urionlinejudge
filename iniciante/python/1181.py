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
    print('{0:.1f}'.format(soma))
else:
    print('{0:.1f}'.format((soma / 12)))
