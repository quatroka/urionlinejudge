#!/usr/bin/env python3
# -*- coding: utf-8 -*-

cases = input()
nums = input().split()
nums = list(map(lambda x: int(x), nums))

mult_2 = 0
mult_3 = 0
mult_4 = 0
mult_5 = 0


for num in nums:
    if num % 2 == 0:
        mult_2 += 1
    if num % 3 == 0:
        mult_3 += 1
    if num % 4 == 0:
        mult_4 += 1
    if num % 5 == 0:
        mult_5 += 1

print('{0} Multiplo(s) de 2'.format(mult_2))
print('{0} Multiplo(s) de 3'.format(mult_3))
print('{0} Multiplo(s) de 4'.format(mult_4))
print('{0} Multiplo(s) de 5'.format(mult_5))
