# -*- coding: utf-8 -*-

choice = 1
while(choice == 1):
    nota1 = 100
    while(nota1 < 0 or nota1 > 10):
        nota1 = float(input())
        if(nota1 < 0 or nota1 > 10):
            print('nota invalida')

    nota2 = 100
    while(nota2 < 0 or nota2 > 10):
        nota2 = float(input())
        if(nota2 < 0 or nota2 > 10):
            print('nota invalida')

    print('media = %.2f' % ((nota1 + nota2) / 2))

    choice = 99
    while(choice == 99):
        print('novo calculo (1-sim 2-nao)')
        choice = int(input())
        if(choice == 2):
            break
        elif(choice != 1):
            choice = 99
        else:
            choice = 1
