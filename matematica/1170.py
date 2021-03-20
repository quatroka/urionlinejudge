cases = int(input())
for _ in range(cases):
    counter = 0
    n = float(input())
    while True:
        n /= 2
        counter += 1
        if n <= 1:
            print(f"{counter} dias")
            break
