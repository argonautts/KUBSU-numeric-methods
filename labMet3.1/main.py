import numpy as np


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


a = np.array([
    [10 ** -4, 1.0],
    [1.0, 2.0]
])
b = np.array([1.0, 4.0])

a_orig = a.copy()
b_orig = b.copy()

x = gauss(a, b)
x_teory = np.array([2, 1])

print('x = ', x)
print('\nНевязка e:', x_teory - x)
print('Невязка r:', b - a @ x)
