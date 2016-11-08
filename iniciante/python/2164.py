#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt

n = int(input())

fibo = ((((1 + sqrt(5)) / 2)**n) - (((1 - sqrt(5)) / 2)**n)) / sqrt(5)

print('{0:.1f}'.format(fibo))
