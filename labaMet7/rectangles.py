import math


def f(x: float) -> float:
    return 2 * math.exp(-x*x) / math.sqrt(math.pi)


def rectangles(n: int, x: float) -> float:
    def g(x: float) -> float:
        return math.exp(-x * x)
    h = x / n
    t = [i * h for i in range(n+1)]
    return sum([2 / math.sqrt(math.pi) * h * g((t[i] + t[i+1]) / 2) for i in range(n)])


x = [i/10 for i in range(21)]
num = [rectangles(32, xi) for xi in x]