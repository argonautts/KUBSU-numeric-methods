import math

def e(n):
    if n == 1:
        return 1 / math.e
    return 1 - n * e(n - 1)

def new_e(n, m):
    if n == m:
        return 1 / (n + 1)
    return (1 - new_e(n + 1, m)) / (n + 1)

n = 15
print(f'E({n}):', e(n), f'\nNew E({n}):', new_e(n, 100 + n))

