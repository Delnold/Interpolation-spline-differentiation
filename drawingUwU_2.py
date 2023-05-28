import numpy as np
import matplotlib.pyplot as plt

def P_1(x):
    return 1820 * pow((x - 1), 2) + 29 * (x - 1) + 4

def P_2(x):
    return 94752 * pow((x - 3), 2) + 7309 * (x - 3) + 7342

def f_x(x):
    return x ** 8 + 3 * (x ** 5) + 2 * x ** 3 - 2

x = np.linspace(1, 5, 100)

y = f_x(x)
y_1 = P_1(x)
y_2 = P_2(x)

plt.figure()
# Show the plot
plt.show()


plt.plot(x, y, label='func(x)')
plt.plot(x, y_1, label='P1(x)')
plt.plot(x, y_2, label='P2(x)')

plt.ylim([0, 1000000])

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Show the plot
plt.show()
