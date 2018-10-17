import numpy as np


# Метод перебора
def count(func, start, end, epsilon):
    a = start
    b = end
    n = (b - a) / epsilon
    x = np.linspace(a, b, n)
    y = func(x)

    minimum = np.min(y)
    return minimum
