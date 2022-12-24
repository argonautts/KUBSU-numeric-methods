def gen_c(alpha: list, beta: list, gamma: list, n: int):
    c = [-gamma[0] / beta[0]]
    for i in range(1, n - 1):
        c.append(-gamma[i] / (alpha[i - 1] * c[i - 1] + beta[i]))
    return c


def gen_d(alpha: list, beta: list, c: list, b: list, n: int):
    d = [b[0] / beta[0]]
    for i in range(1, n - 1):
        d.append((b[i] - alpha[i - 1] * d[i - 1]) / (alpha[i - 1] * c[i - 1] + beta[i]))
    return d


def solve(a: list, b: list):
    n = len(b)

    alpha = [a[i][0] for i in range(1, n)]
    beta = [a[0][0]] + [a[i][1] for i in range(1, n)]
    gamma = [a[0][1]] + [a[i][2] for i in range(1, n - 1)]

    c = gen_c(alpha, beta, gamma, n)
    d = gen_d(alpha, beta, c, b, n)

    x = [(b[-1] - alpha[-1] * d[-1]) / (alpha[-1] * c[-1] + beta[-1])]
    for i in range(n - 1):
        x.append(c[-1 - i] * x[-1 - i] + d[-1 - i])

    return x[::-1]


a = [
    [1, 3],
    [-2, 4, -1],
    [2, -2, 1],
    [1, 1, 1],
    [3, -1]
]

b = [
    5,
    1,
    3,
    -2,
    -1
]

x = solve(a, b)

print( "x(itog) = ", x)

