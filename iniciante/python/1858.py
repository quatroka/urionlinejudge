_ = input()
tries = [int(n) for n in input().split()]
minimum = min(tries)
print(tries.index(minimum) + 1)
