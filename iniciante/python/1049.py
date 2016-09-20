# -*- coding: utf-8 -*-

subfilo = input()
tipo = input()
alimento = input()

if subfilo == 'vertebrado':
    if tipo == 'ave':
        if alimento == 'carnivoro':
            print('aguia')
        elif alimento == 'onivoro':
            print('pomba')
    elif tipo == 'mamifero':
        if alimento == 'onivoro':
            print('homem')
        elif alimento == 'herbivoro':
            print('vaca')
elif subfilo == 'invertebrado':
    if tipo == 'inseto':
        if alimento == 'hematofago':
            print('pulga')
        elif alimento == 'herbivoro':
            print('lagarta')
    elif tipo == 'anelideo':
        if alimento == 'hematofago':
            print('sanguessuga')
        elif alimento == 'onivoro':
            print('minhoca')
