import math


def f(x: float) -> float:
    return 2 * math.exp(-x*x) / math.sqrt(math.pi)


def euler(x: list[float], u0: float, t: float) -> float:
    y = [u0, ]
    n = len(x)
    for i in range(n-1):
        y.append(y[i] + t*f(x[i]))
    return y[-1]


x = [i/10 for i in range(21)]
d = [euler(x[:i+1], 0, 0.1) for i in range(len(x))]
