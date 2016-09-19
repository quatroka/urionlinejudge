# -*- coding: utf-8 -*-

choice = 1
inter = 0
gremio = 0
cont = 0
empates = 0

while(choice == 1):
    line = input().split()

    if(line[0] == line[1]):
        empates += 1
    elif(line[0] > line[1]):
        inter += 1
    else:
        gremio += 1

    cont += 1
    choice = 99
    while(choice == 99):
        print('Novo grenal (1-sim 2-nao)')
        choice = int(input())
        if(choice == 2):
            break
        elif(choice != 1):
            choice = 99
        else:
            choice = 1

print('%s grenais' % cont)
print('Inter:%s' % inter)
print('Gremio:%s' % gremio)
print('Empates:%s' % empates)

if(gremio > inter):
    print('Gremio venceu mais')
elif(gremio < inter):
    print('Inter venceu mais')
else:
    print('Nao houve vencedor')
