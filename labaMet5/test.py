import numpy as np


def Lagrange(x:float, xk:list[float], f:dict[float, float]):
    s = 0
    n = len(xk)
    for k in range(n):
        p1 = 1
        for i in range(n):
            if i != k:
                p1 *= x - xk[i]
        p2 = 1
        for i in range(n):
            if i != k:
                p2 *= xk[k] - xk[i]
        s += p1 / p2 * f[xk[k]]
    return s


def f(x:list[float], func:dict[float, float]):
    s = 0
    n = len(x)
    for i in range(n):
        p = 1
        for j in range(n):
            if j != i:
                p *= x[i] - x[j]
        s += func[x[i]] / p
    return s


def Newton(x:float, xk:list[float], func:dict[float, float]):
    s = 0
    n = len(xk)
    for i in range(n):
        p = 1
        for j in range(i):
            p *= x - xk[j]
        s += p * f(xk[:i+1], func)
    return s


for i in [(x*2, y) for x, y in enumerate(range(0, 40, 4))]:
    print(i)

