import math


def f(x: float) -> float:
    return math.exp(-x*x)


def rectangles(n: int, x: float) -> float:
    h = x / n
    t = [i * h for i in range(n+1)]
    return sum([2 / math.sqrt(math.pi) * h * f((t[i] + t[i+1]) / 2) for i in range(n)])


x = [i / 10 for i in range(21)]

for xi in x:
    r = rectangles(1024, xi)
    print("x[i]:", xi)
    print("Numerical:", r, ", error:", math.erf(xi)," : ", r - math.erf(xi), end="\n\n")
