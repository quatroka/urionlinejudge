# -*- coding: utf-8 -*-

i = 1
j = 7

while(i != 11):
    print('I=%s J=%s' % (i, j))
    j -= 1
    if(j == (i + 3)):
        j = j + 5
        i += 2
