def gen_c(alpha:list[float], beta:list[float], gamma:list[float], n:int):
    c = [-gamma[0]/beta[0]]
    for i in range(1,n-1):
        c.append(-gamma[i] / (alpha[i-1] * c[i-1] + beta[i]))
    return c
        

def gen_d(alpha:list[float], beta:list[float], c:list[float], b:list[float], n:int):
    d = [b[0]/beta[0]]
    for i in range(1,n-1):
        d.append((b[i] - alpha[i-1]*d[i-1]) / (alpha[i-1]*c[i-1] + beta[i]))
    return d


def solve(alpha:list[float], beta:list[float], gamma:list[float], b:list[float]):
    n = len(b)
    
    c = gen_c(alpha, beta, gamma, n)
    d = gen_d(alpha, beta, c, b, n)
    
    x = [(b[-1]-alpha[-1]*d[-1])/(alpha[-1]*c[-1]+beta[-1])]
    for i in range(n-1):
        x.append(c[-1-i] * x[-1-i] + d[-1-i])
    
    
    return x[::-1]

