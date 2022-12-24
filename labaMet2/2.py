import math

def solve1(case):
    a, b, c = case[0], case[1], case[2]
    d = b * b - 4 * a * c
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return (x1, x2)


def solve2(case):
    a, b, c = case[0], case[1], case[2]
    d = b * b - 4 * a * c
    x1 = -(b + (1 if b > 0 else -1) * math.sqrt(d)) / (2 * a)
    x2 = c / (a * x1)
    return (x1, x2)



cases = [
    (1, -1 * 10 ** 5, 1),
    (6, 5, -4),
    (6 * 10 ** 30, 5 * 10 ** 30, -4 * 10 ** 30),
    (10 ** -30, -10 ** 30, 10 ** 30),
    (1.0000000, -4.0000000, 3.9999999)
]

for case in cases:
    print('Case:', ', '.join(map(str, case)),
          '\nMethod 1:', ', '.join(map(str,solve1(case))),
          '\nMethod 2:', ', '.join(map(str,solve2(case))), '\n')
