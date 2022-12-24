import math


def f(_f: float, _r: float, _a: float) -> float:
    return -_f + _a * _r * _f


def r(_f: float, _r: float, _a: float) -> float:
    return 2 * _r - _a * _r * _f

# Метод Эйлера для пропорций
def euler(t: list[float], _f0: float, _r0: float, _a: float) -> tuple[list[float], list[float]]:
    res_f, res_r = [_f0], [_r0]
    for i in range(1, len(t)):
        h = t[i] - t[i-1]
        res_r.append(math.floor(res_r[i-1]+h*r(res_f[i-1], res_r[i-1], _a)))
        res_f.append(math.floor(res_r[i-1]+h*f(res_f[i-1], res_r[i-1], _a)))
        if res_r[-1] <= 0 or res_f[-1] <= 0:
            res_r[-1] = 0 if res_r[-1] < 0 else res_r[-1]
            res_f[-1] = 0 if res_f[-1] < 0 else res_f[-1]
            break
    return res_r, res_f


A = 0.01  # alpha
base_values = [(2**i, 2**i) for i in range(1, 17)]

for r0, f0 in base_values:
    rabbits, foxes = euler(range(10), f0, r0, A)

    print("Лисы - Кролики")
    print("\n".join([str(fi) + " - " + str(ri) for fi, ri in zip(foxes, rabbits)]), "\n")
