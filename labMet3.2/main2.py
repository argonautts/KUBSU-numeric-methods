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


def gauss2(a, b):
    n = len(b)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            lam = a[i, k] / a[k, k]
            a[i, k:n] -= lam * a[k, k:n]
            b[i] -= lam * b[k]
    if (np.linalg.matrix_rank(a) < n):
        r = n - np.linalg.matrix_rank(a)
        print('Свободные переменные:', ' '.join(['x' + str(n - i) for i in range(r)]))
        i = 0
        for k in range(0, n):
            if sum(np.around(a[k, k:n], decimals=10)) == 0.0:
                a = np.copy(np.delete(a, axis=0, obj=i))

            else:
                i += 1
        for i in range(r):
            b[n - 1 - i] = 1
        for k in range(n - 1 - r, -1, -1):
            b[k] = (b[k] - np.dot(a[k, k + 1:n], b[k + 1:n])) / a[k, k]
    else:
        for k in range(n - 1 - r, -1, -1):
            b[k] = (b[k] - np.dot(a[k, k + 1:n], b[k + 1:n])) / a[k, k]
    return b


def cond(a, x):
    ax = a @ x
    return max(map(abs, ax / x)) / min(map(abs, ax / x))


a = np.array([
    [0.1, 0.2, 0.3],
    [0.4, 0.5, 0.6],
    [0.7, 0.8, 0.9]
])
b = np.array([0.1, 0.3, 0.5])
a_orig = np.copy(a)

print('X:' + ' '.join([str(x) for x in gauss2(a, b)]))
print('A:\n' + '\n'.join([' '.join([str(aij) for aij in np.around(ai, decimals=10)]) for ai in a]))

