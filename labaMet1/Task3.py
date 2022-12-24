import math

e = 3 * 10 ** -8

def s(x):
    k = 1
    s1 = 1 / math.sqrt(1 + x)
    olds1 = s1 - 1
    s2 = 1 / math.sqrt(1 - x)
    olds2 = s2 - 1
    
    while (abs(s1 - olds1) > e / 10):
        olds1 = s1
        k = k + 1
        s1 = s1 + 1 / math.sqrt(k ** 3 + x)
    
    k = 1
    
    while (abs(s2 - olds2) > e / 10):
        olds2 = s2
        k = k + 1
        s2 = s2 + 1 / math.sqrt(k ** 3 - x)
        
    return s1 - s2


x = 0.999999999

print('S(x) = ', s(x), ', x = ', x, sep='')
        
    