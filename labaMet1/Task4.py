import math

e = 10 ** -10

def s():
    n = 1
    s = 1 / 2 + math.pi ** 2 / 6 - math.pi ** 4 / 90
    olds = s - 1
    while(abs(s - olds) > e / 10):
        olds = s
        n = n + 1
        s = s + 1 / ((n ** 4) * ((n ** 2) + 1))
    return s


print('S =', s())

