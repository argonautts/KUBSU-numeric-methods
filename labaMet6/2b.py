import math

import tma


def f(x: float) -> float:
    return 4 / (1 + x ** 2)


def splain(n: int) -> float:
    h = 1.0 / n
    x = [i*h for i in range(n+1)]
    fx = [f(xi) for xi in x]
    c = [0] + tma.solve(
        alpha=x[:-1],
        beta=[2 * (x[i - 1] + x[i]) for i in range(1, n - 1)],
        gamma=x,
        b=[(fx[i + 1] - fx[i]) / h - (fx[i] - fx[i - 1]) / h
           for i in range(1, n - 1)]) + [0]
    return sum([h * (f(x[i]) + f(x[i+1])) / 2 - h ** 3 * (c[i] + c[i+1]) / 12 for i in range(n-1)])


n = [8, 32, 128]

for ni in n:
    s = splain(ni)
    print("h^2:", (1.0 / ni) ** 2)
    print("Splain:", s, ", error:", math.pi - s)
