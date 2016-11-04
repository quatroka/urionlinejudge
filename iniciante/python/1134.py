# -*- coding: utf-8 -*-

alcool = 0
gasolina = 0
diesel = 0

choice = 0
while choice != 4:
    choice = int(input())
    if choice == 1:
        alcool += 1
    elif choice == 2:
        gasolina += 1
    elif choice == 3:
        diesel += 1
    elif choice == 4:
        break

print('MUITO OBRIGADO')
print('Alcool: {0!s}'.format(alcool))
print('Gasolina: {0!s}'.format(gasolina))
print('Diesel: {0!s}'.format(diesel))
