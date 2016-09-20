# -*- coding: utf-8 -*-

line = input().split()

if int(line[0]) % int(line[1]) == 0 or int(line[1]) % int(line[0]) == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
