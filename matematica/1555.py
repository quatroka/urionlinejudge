def rafa(x, y):
    return (3**2 * x**2) + (y ** 2)


def beto(x, y):
    return (2 * x ** 2) + (5 ** 2 * y ** 2)


def carlos(x, y):
    return (-100 * x) + y ** 3


for _ in range(int(input())):
    line = input().split()
    x, y = int(line[0]), int(line[1])
    values = [rafa(x, y), beto(x, y), carlos(x, y)]
    max_value = max(values)
    if values.index(max_value) == 0:
        print('Rafael ganhou')
    elif values.index(max_value) == 1:
        print('Beto ganhou')
    else:
        print('Carlos ganhou')
