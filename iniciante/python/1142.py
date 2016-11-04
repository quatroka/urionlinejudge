# -*- coding: utf-8 -*-

x = int(input()) * 4
for x in range(1, x, 4):
    print("{0!s} {1!s} {2!s} PUM".format(str(x), str(x + 1), str(x + 2)))
