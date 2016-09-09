# -*- coding: utf-8 -*-

alcool = 0
gasolina = 0
diesel = 0

choice = 0
while(choice != 4):
    choice = int(input())
    if(choice == 1):
        alcool += 1
    elif(choice == 2):
        gasolina += 1
    elif(choice == 3):
        diesel += 1
    elif(choice == 4):
        break

print('MUITO OBRIGADO')
print('Alcool: %s' % alcool)
print('Gasolina: %s' % gasolina)
print('Diesel: %s' % diesel)
