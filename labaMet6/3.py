import math

import numpy as np
import scipy.special


def f(x: float) -> float:
    return math.exp(x * x) if x <= 2 else 1 / (4 - math.sin(16 * math.pi * x))


def analytic(a: float, b: float) -> float:
    if a < 2:
        return math.sqrt(math.pi) / 2 * (scipy.special.erfi(b) - scipy.special.erfi(a))

    return scipy.integrate.quad(lambda x: 1 / (4 - np.sin(16 * np.pi * x)), 2, 4)[0]


def main_simpson(x: list[float]) -> float:
    h = x[1] - x[0]
    return sum([h / 6 * (f(xi) + 4 * f(xi + h / 2) + f(xi + h)) for xi in x])


def compos_simpson(x: list[float]) -> float:
    h = x[1] - x[0]
    return sum(
        [h / 12 * (f(xi) + 4 * f(xi + h / 4) + 2 * f(xi + h / 2) + 4 * f(xi + 3 * h / 4) + f(xi + h)) for xi in x])


def rectangles(x: list[float]) -> float:
    h = x[1] - x[0]
    return sum([h * f((x[i] + x[i+1]) / 2) for i in range(len(x)-1)])


def trapezoid(x: list[float]) -> float:
    h = x[1] - x[0]
    return sum([h * (f(x[i]) + f(x[i+1])) / 2 for i in range(len(x)-1)])


def numeric_method(x: list[float], e: float) -> float:
    a = analytic(x[0], x[-1])
    compos = compos_simpson(x)
    main = main_simpson(x)
    if abs(main - a) < e and abs(main - a) < abs(compos - a):
        return main
    if abs(compos - a) < e:
        return compos
    if len(x) < 4:
        return main if abs(main - a) <= abs(compos - a) else compos
    return numeric_method(x[:2], e) + numeric_method(x[2:], e)


def numeric_method1(x: list[float], e: float) -> float:
    a = analytic(x[0], x[-1])
    num = (
        rectangles(x),
        trapezoid(x),
        main_simpson(x),
        compos_simpson(x)
    )
    exact = [i for i in num if abs(i-a) < e]
    if exact:
        return min(exact)
    if len(x) < 4:
        return min([(abs(i-a), i) for i in num])[1]
    return numeric_method(x[:2], e) + numeric_method(x[2:], e)


n, error = 400, 1
nods = [4 * i / n for i in range(n + 1)]
num = numeric_method(nods[:n // 2], error) + numeric_method(nods[n // 2:], error)
an = analytic(0, 2) + analytic(2, 4)

print("Numeric:", num)
print("Analytic:", an)
print("Diff:", abs(num - an))
