import math
import matplotlib.pyplot as plt


T, L = 0.0069, math.pi / 2
M, N = 100, 100


def difference_method(n: int, m: int) -> list[list[float]]:
    """
    Неявный разностный метод при сигме равной 1/4
    :param n: число вертикальных разбиений сетки
    :param m: число горизонтальных разбиений сетки
    :return: значение разностной аппроксимации в узлах сетки
    """
    h = L / n  # шаг по времени
    tau = T / m  # шаг по пространству

    x = [i * h for i in range(n + 1)]
    t = [j * tau for j in range(m + 1)]
    y = [[0 for i in range(n + 1)] for j in range(m + 1)]
    y[0] = [math.sin(i) for i in x]

    for j in range(1, m + 1):
        alpha = [0 for _ in range(n + 1)]
        beta = [0 for _ in range(n + 1)]
        alpha[0], beta[0] = 0, 0
        # прямая прогонка
        for i in range(1, n + 1):
            alpha[i] = tau / (2 * tau + 4 * h ** 2 - alpha[i - 1] * tau)
            beta[i] = (tau * beta[i - 1] + 3 * tau * y[j - 1][i] +
                       (4 * h ** 2 - 6 * tau) * y[j - 1][i - 1] +
                       3 * tau * y[j - 1][i - 2]) / (2 * tau + 4 * h ** 2 - alpha[i - 1] * tau)
        y[j][n] = math.exp(-t[j])
        # обратная прогонка
        for i in range(n - 1, 0, -1):
            y[j][i] = alpha[i + 1] * y[j][i + 1] + beta[i + 1]
    return y


def analytic_method(n: int, m: int) -> list[list[float]]:
    return [[math.exp(-j * T / m) * math.sin(math.pi / 2 * i / n) for i in range(n + 1)] for j in range(m + 1)]


analytic = analytic_method(N, M)
diff = difference_method(N, M)

dots = [i / N * math.pi / 2 for i in range(N + 1)]
plt.scatter(dots, diff[-1], color="lime", label="Разностный метод")
plt.plot(dots, analytic[-1], color="green", label="Аналитический метод")
plt.legend()
plt.grid(linestyle='-.')
plt.show()
