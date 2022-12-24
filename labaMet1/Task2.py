import math

def Phi2(x):
    c = 0
    k = 2
    olds = 1 - 1 / (1 + x)
    s = olds + 1 / k - 1 / (k + x)
    while(abs(s - olds) > 10 ** -9):
        k = k + 1
        olds = s
        s = olds + 1 / k - 1 / (k + x)
        c += 1
    print('C2 =', c)
    return s

def Phi1(x):
    c = 0
    k = 2
    olds = 1 / (1 + x)
    s = olds + 1 / (k * (k + x))
    while(abs(s - olds) > 10 ** -9):
        k = k + 1
        olds = s
        s = olds + 1 / (k * (k + x))
        c += 1
    print('C1 =', c)
    return s


x = [xi / 10 for xi in range(0, 10 + 1)]
for xi in x:
    print('x = ', xi)
    print('Phi1(x) = ', Phi1(xi))
    print('Phi2(x) = ', Phi2(xi), end='\n\n')

