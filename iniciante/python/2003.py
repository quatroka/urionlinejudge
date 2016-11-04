# -*- coding: utf-8 -*-

while True:
    try:
        n = input()

        horas = int(n[0:1])
        minutos = int(n[2:])

        atraso = 0
        if horas >= 7:
            atraso = (horas - 7) * 60 + minutos
        print('Atraso maximo: {0!s}'.format(atraso))
    except EOFError:
        break
