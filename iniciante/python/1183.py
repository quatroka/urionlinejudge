# -*- coding: utf-8 -*-

operation = input()

matriz = []

for i in range(0, 12):
    matriz_aux = []

    for j in range(0, 12):
        matriz_aux.append(float(input()))

    matriz.append(matriz_aux)

soma = 0
elementos = 0
for k in range(0, len(matriz)):
    for l in range(k + 1, len(matriz)):
        soma += matriz[k][l]
        elementos += 1


if operation == 'S':
    print('{0:.1f}'.format(soma))
else:
    print('{0:.1f}'.format((soma / elementos)))
