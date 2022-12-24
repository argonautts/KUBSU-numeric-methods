import numpy as np
import matplotlib.pyplot as plt

# Switch Jacobi to current file

def Seidel(A, b, e):
    n = b.shape[0]
    x_old = np.zeros_like(b)
    errors = []

    converage = False
    while not converage:
        x_new = np.zeros_like(x_old)
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x_old[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]

        errors.append(max(x_new - x_old))
        converage = np.allclose(x_new, x_old, atol=e, rtol=0.)
        x_old = x_new

    return (x_old, errors)


A = np.array([
    [12.14, 1.32, -0.78, -2.75],
    [-0.89, 16.75, 1.88, -1.55],
    [2.65, -1.27, -15.64, -0.64],
    [2.44, 1.52, 1.93, -11.43]
])

B = np.array([
    14.78,
    -12.14,
    -11.65,
    4.26
])

E = 1e-10
x, errors = Seidel(A, B, E)

print(x)
print('\n'.join([str(i + 1) + ": " + str(errors[i]) for i in range(len(errors))]))

plt.plot(range(1, len(errors) + 1), errors, 'o:r')
plt.xticks(range(1, len(errors) + 1))
plt.grid()

plt.title('The Seidel method')
plt.xlabel('Iteration number')
plt.ylabel('The discrepancy rate')

plt.show()

