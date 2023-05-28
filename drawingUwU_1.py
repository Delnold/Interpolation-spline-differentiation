import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 126358 - 271722*x + 200365*x**2 - 61993*x**3 + 6996*x**4

def g(x):
    return x**8 + 3*x**5 + 2*x**3 - 2

x = np.linspace(1, 5, 100)

y1 = f(x)
y2 = g(x)

plt.figure()

plt.plot(x, y1, label='func(x)')
plt.plot(x, y2, label='interpolation(x)')

plt.ylim([0, 1000000])

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.show()
