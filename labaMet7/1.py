import timeit

from euler import *
from rectangles import *


with open("euler.py", "r") as f:
    code_d = f.read()

with open("rectangles.py", "r") as f:
    code_n = f.read()


print('Differential - numeric - difference')
print('\n'.join([str(di)+' - '+str(ni)+' - '+str(abs(di-ni)) for di, ni in zip(d, num)]))
t1, t2 = timeit.timeit(code_d, number=1), timeit.timeit(code_n, number=1)
print("Time differential:", t1, "\nTime numeric:", t2, "\nTime difference:", abs(t2-t1))
