    # -*- coding: utf-8 -*-

    line = input().split()

    a = float(line[0])
    b = float(line[1])

    print('%.2f%%' % (b / a * 100 - 100))
