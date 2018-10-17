import numpy as np
import matplotlib.pyplot as plt


# Метод перебора
def count(func, start, end, epsilon, show_chart=False):
    a = start
    b = end
    n = (b - a) / epsilon
    x = np.linspace(a, b, n)
    y = func(x)

    if show_chart:
        plt.scatter(x, y, color='c')

    min_index = np.argmin(y)

    plt.scatter(x[min_index], y[min_index], color='red')
    return y[min_index]
