# -*- coding: utf-8 -*-

NAME, SALARY, SELLS = input(), float(input()), float(input())
TOTAL = SELLS * 0.15 + SALARY
print("TOTAL = R$ {0:.2f}".format(TOTAL))
