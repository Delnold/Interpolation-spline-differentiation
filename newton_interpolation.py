def func(x: int):
    return pow(x, 8) + 3 * pow(x, 5) + 2 * pow(x, 3) - 2

def newton_interpolation(x_values, func_values):
    counter = 0
    n = len(x_values)
    f = [[None] * n for i in range(n)]

    for i in range(n):
        f[i][0] = func_values[i]

    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (x_values[i + j] - x_values[i])

    print("Iterative table:")
    print("\t\t\t\t")
    for row in f:
        for elem in row:
            if elem is not None:
                print(f"{elem:8.4f}", end="\t")
            else:
                print("\t", end="")
        print()


x_values = [1, 2, 3, 4, 5]
func_values = [func(x) for x in x_values]
newton_interpolation(x_values, func_values)
