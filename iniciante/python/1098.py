from decimal import Decimal

i = 0
j = 1
while i <= 2:
    if i / 2 == 0 or i / 2 == 0.5 or i / 2 == 1:
        print('I=%.0f J=%.0f' % (i, j))
    else:
        print('I={} J={}'.format(i, j))
    j += 1
    if j == (i + 4):
        i = i + Decimal('0.2')
        j = j - Decimal('2.8')
