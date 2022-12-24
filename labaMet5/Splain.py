import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import solveForSplain as tma

# Switch main on current file

def splain(x:float, nodes:list[float], fx:list[float]) -> float:
    n = len(nodes)
    h = [nodes[i] - nodes[i-1] for i in range(1, n)]
    
    c = [0] + tma.solve(
                  alpha=h[:-1],
                  beta=[2*(h[i-1] + h[i]) for i in range(1, n-1)],
                  gamma=h,
                  b=[(fx[i+1] - fx[i]) / h[i] - (fx[i] - fx[i-1]) / h[i-1]
                     for i in range(1, n-1)]) + [0]
    
    d = [(c[i] - c[i-1]) / h[i-1] for i in range(1, n)]
    b = [h[i-1] * c[i] / 2 - h[i-1]**2 * d[i-1] / 6 + (fx[i] - fx[i-1]) / h[i-1]
         for i in range(1, n)]
    a = fx

    for i in range(n-1):
        if nodes[i] <= x <= nodes[i+1]:
            y = x - nodes[i]
            return a[i] + b[i] * y + c[i] * y**2 + d[i] * y**3
    if x > nodes[n-2]:
        y = x - nodes[n-2]
        return a[n-2] + b[n-2] * y + c[n-2] * y**2 + d[n-2] * y**3
    y = x - nodes[0]
    return a[0] + b[0] * y + c[0] * y**2 + d[0] * y**3
    


def f(x:float) -> float:
    return 1 / (1 + 25*x**2)


a, b = (-1, 1)
n = (10, 50, 100)
dots = [a + (b-a)*h/20 for h in range(21)]

for i in range(len(n)):
    nodes = [a + h*(b-a)/n[i] for h in range(n[i])]
    plt.subplot(1, 4, i + 1)
    plt.plot(dots, [f(x) for x in dots], 'b',
             dots, [splain(x, nodes, [f(y) for y in nodes]) for x in dots], 'r--')
    plt.title('n = ' + str(n[i]))

fx = {2:4, 3:-2, 5:6, 7:-3}

plt.subplot(1, 4, 4)
plt.plot(fx.keys(), fx.values(), 'b',
         fx.keys(), [splain(x, list(fx.keys()), list(fx.values())) for x in fx.keys()], 'o--r')
plt.title('Cubic Table spline')

plt.suptitle('Cubic spline of the function f(x)'+' '*10)
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
legend = [mpatches.Patch(color='blue', label='f(x)'), mpatches.Patch(color='red', label='S(x)')]
plt.legend(handles=legend)
plt.show()



