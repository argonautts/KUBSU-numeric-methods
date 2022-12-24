import numpy as np
import math

def erf(x):
    n = 0
    s = 2 / math.sqrt(math.pi) * x
    t = s
    olds = s - 1
    while (s != olds):
        olds = s
        n = n + 1
        t = -1 * t * (x ** 2) * (2 * n - 1) / (n * (2 * n + 1))
        s = s + t
    return s if s < 1.0 else 1.0


def gauss(a, b):
    n = len(b)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if a[i, k] != 0.0:
                lam = a[i, k] / a[k, k]
                a[i, k + 1:n] = a[i, k + 1:n] - lam * a[k, k + 1:n]
                b[i] = b[i] - lam * b[k]

    for k in range(n - 1, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k + 1:n], b[k + 1:n])) / a[k, k]
    return b


def cond(a, x):
    ax = a @ x
    return max(map(abs, ax / x)) / min(map(abs, ax / x))


a = np.array([
    [1.00, 0.80, 0.64],
    [1.00, 0.90, 0.81],
    [1.00, 1.10, 1.21]
])
b = np.array([erf(0.80), erf(0.90), erf(1.10)])

x = gauss(a, b)

print("Число обусловленности", cond(a, x)) # вычисляем число обусловленности
print('x1, x2, x3:', x)
print('x1 + x2 + x3 = ', sum(x))
print('erf(1.0) = ', erf(1.0))

