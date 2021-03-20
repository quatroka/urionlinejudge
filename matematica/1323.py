while True:
    n = int(input())
    if n == 0:
        break
    print(sum(i ** 2 for i in range(n, 0, -1)))
