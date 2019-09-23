tries = int(input())
for _ in range(tries):
    year = int(input())
    if year < 2015:
        print("{} D.C.".format(2015 - year))
    else:
        print("{} A.C.".format(abs(year - 2014)))
