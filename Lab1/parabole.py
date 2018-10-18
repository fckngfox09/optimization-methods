import numpy as np
import matplotlib.pyplot as plt


# Метод парабол
def count(func, start, end, epsilon, show_chart=False):
    a = start
    b = end

    x1 = a
    x2 = (a + b) / 2
    x3 = b

    f1 = func(x1)
    f2 = func(x2)
    f3 = func(x3)

    x0, x1, x2, x3, f1, f2, f3 = on_count(func, x1, x2, x3, f1, f2, f3, a, b, show_chart)

    iter_count = 1
    while True:
        x_iter, x1, x2, x3, f1, f2, f3 = on_count(func, x1, x2, x3, f1, f2, f3, a, b, show_chart)
        delta = np.abs((x0 - x_iter))
        x0 = x_iter
        if np.abs(delta <= epsilon):
            break
        iter_count += 1

    if show_chart:
        plt.scatter(x0, func(x0), color='red')

    return func(x0), iter_count


def on_count(func, x1, x2, x3, f1, f2, f3, a, b, show_chart):
    a0 = f1
    a1 = (f2 - f1) / (x2 - x1)
    a2 = ((f3 - f1) / (x3 - x1) - (f2 - f1) / (x2 - x1)) / (x3 - x2)

    x = (x1 + x2 - a1 / a2) / 2

    y_plot = (lambda q: a0 + a1 * (q - x1) + a2 * (q - x1) * (q - x2))
    x_plot = np.linspace(a, b, 200)
    y_p = y_plot(x_plot)

    if show_chart:
        plt.plot(x_plot, y_p)

    fx = func(x)

    if x > x2 and fx > f2:
        x3, f3 = x, fx
    elif x > x2 and fx < f2:
        x1, f1 = x2, f2
        x2, f2 = x, fx
    elif x < x2 and fx > f2:
        x1, f1 = x, fx
    elif x < x2 and fx < f2:
        x3, f3 = x2, f2
        x2, f2 = x, fx

    return x, x1, x2, x3, f1, f2, f3
