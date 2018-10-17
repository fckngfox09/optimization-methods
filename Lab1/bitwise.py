import numpy as np
import matplotlib.pyplot as plt


# Поразрядный поиск
def count(func, start, end, delta, epsilon, show_chart=False):
    x = start
    y = func(x)

    x_old = x
    y_old = y
    iter_count = 0

    mul_const = -4

    while np.abs(delta * mul_const) > epsilon:
        x, y, iter_count = on_count(func, x, delta, y, iter_count)

        # Постройка графика
        if show_chart:
            plt.plot([x_old, x], [y_old, y])
            x_old = x
            y_old = y

        delta /= mul_const

    return y, iter_count


def on_count(func, x, delta, y_old, iter_count):
    x += delta
    y_new = func(x)
    iter_count += 1

    while y_new < y_old:
        y_old = y_new
        x += delta
        y_new = func(x)
        iter_count += 1

    return x, y_new, iter_count
