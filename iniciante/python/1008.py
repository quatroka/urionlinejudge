# -*- coding: utf-8 -*-

NUMBER, WON, HOURS = int(input()), int(input()), float(input())
SALARY = float(WON * HOURS)
print("NUMBER = %a" % NUMBER)
print("SALARY = U$ {0:.2f}".format(SALARY))
