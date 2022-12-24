import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import math

def Lagrange(x:float, nodes:list[float]):
    s = 0
    for xi in nodes:
        p = f(xi)
        for xk in nodes:
            if xi != xk:
                p *= (x - xk) / (xi - xk)
        s += p
    return s
                

def f(x:float) -> float:
    return 1 / (1 + 25*x**2)


def equidistant_nodes(a:float, b:float, n:int) -> list[float]:
    return [a + i * (b - a) / n for i in range(n+1)]


def chebyshev_nodes(a:float, b:float, n:int) -> list[float]:
    return [(a + b) / 2 + (b - a) * math.cos((2*i+1)*math.pi/(2*n+2)) / 2 for i in range(n+1)]


a, b = (-1, 1)
n = (5, 10, 50)
dots = [a + h*0.04 for h in range(51)]


for i, ni in [(ei*2, e) for ei, e in enumerate(n)]:
    eqn = equidistant_nodes(a, b, ni)
    plt.subplot(3, 2, i + 1)
    plt.plot(dots, [f(x) for x in dots], 'b', dots, [Lagrange(x, eqn) for x in dots], 'r--')
    plt.title('n = ' + str(ni))
    
    chn = chebyshev_nodes(a, b, ni)
    plt.subplot(3, 2, i + 2)
    plt.plot(dots, [f(x) for x in dots], 'b', dots, [Lagrange(x, chn) for x in dots], 'r--')
    plt.title('n = ' + str(ni))


plt.suptitle('Равноотстоящие узлы'+' '*20 +'Чебышевские узлы')
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
legend = [mpatches.Patch(color='blue', label='f(x)'), mpatches.Patch(color='red', label='L(x)')]
plt.legend(handles=legend)
plt.show()

