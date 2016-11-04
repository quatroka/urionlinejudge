# -*- coding: utf-8 -*-

casos = int(input())

for i in range(0, casos):
    num = str(input())
    leds = 0
    for j in range(0, len(num)):
        if num[j] == '1':
            leds += 2
        elif num[j] == '2' or num[j] == '3' or num[j] == '5':
            leds += 5
        elif num[j] == '4':
            leds += 4
        elif num[j] == '6' or num[j] == '9' or num[j] == '0':
            leds += 6
        elif num[j] == '7':
            leds += 3
        elif num[j] == '8':
            leds += 7

    print('{0:d} leds'.format(leds))
