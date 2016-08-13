# -*- coding: utf-8 -*-

line = input().split()

a = line[0]
b = line[1]
c = line[2]

line[0] = int(line[0])
line[1] = int(line[1])
line[2] = int(line[2])

for i in range(0, 3):
    for j in range(0, 3):
        if(line[i] < line[j]):
            aux = line[j]
            line[j] = line[i]
            line[i] = aux

print(line[0])
print(line[1])
print(line[2])
print('')
print(a)
print(b)
print(c)
