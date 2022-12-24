import sympy as sym
import numpy as np

x = sym.Symbol('x')
# Метод Ньютона (метод касательных) — это итерационный численный метод нахождения корня (нуля) заданной функции.

# Достоинства метода Ньютона: Метод Ньютона - самый быстрый способ нахождения корней уравнений:
# обычно заданная точность достигается за 2-3 итерации.
# Очень быстрая сходимость по сравнению с методом половинного деления и методом простой итерации к заданной точности.

# Недостаток: громоздкий алгоритм: на каждой итерации необходимо вычислять значение функции и ее первой производной.


# a = 1, b = 3, c = 4, d = 3*4
f = x ** 3 + 3*x ** 2 + 4 * x + 21

diff_f = sym.diff(f, x)
diff_f

f_func = sym.lambdify(x, f, 'numpy')
diff_f_func = sym.lambdify(x, diff_f, 'numpy')


def newtonMethod(x0, iterationNumber, f, df):
    x = x0

    for i in range(iterationNumber):
        x = x - f(x) / df(x)

    residual = np.abs(f(x))
    return x, residual


solution, residual = newtonMethod(-2, 200, f_func, diff_f_func)
print(solution)