import math


def f(x: float) -> float:
    return 4 / (1 + x ** 2)


def rectangles(n: int) -> float:
    h = 1.0 / n
    x = [i * h for i in range(n+1)]
    return sum([h * f((x[i] + x[i+1]) / 2) for i in range(n-1)])


def trapezoid(n: int) -> float:
    h = 1.0 / n
    x = [i * h for i in range(n+1)]
    return sum([h * (f(x[i]) + f(x[i+1])) / 2 for i in range(n-1)])


n = [8, 32, 128]

for ni in n:
    r = rectangles(ni)
    t = trapezoid(ni)
    print("h^2:", (1.0 / ni) ** 2)
    print("Rectangles:", r, ", error:", math.pi - r)
    print("Trapezoid:", t, ", error:", math.pi - t, end="\n\n")
