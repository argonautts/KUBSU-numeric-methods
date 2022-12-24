import math

def erf(x):
    n = 0
    s = 2 / math.sqrt(math.pi) * x
    t = s
    olds = s - 1
    while(s != olds):
        olds = s
        n = n + 1
        t = -1 * t * (x ** 2) * (2*n - 1) / (n * (2*n + 1))
        s = s + t
    return s if s < 1.0 else 1.0

x = (0.5, 1.0, 5.0, 10.0)
for xi in x:
    print('erf(x)= ', erf(xi), ', x = ', xi, sep='')
