import numpy as np
import matplotlib.pyplot as plt


# Метод золотого сечения
def count(func, start, end, epsilon, show_chart=False):
    a = start
    b = end

    x1 = a + ((3 - np.sqrt(5)) / 2) * (b - a)
    x2 = a + ((np.sqrt(5) - 1) / 2) * (b - a)

    y1 = func(x1)
    y2 = func(x2)

    tau = (np.sqrt(5) - 1) / 2
    epsilon_n = (b - a) / 2

    iter_count = 1
    while epsilon_n > epsilon:
        a, b, x1, y1, x2, y2, epsilon_n = on_count(func, a, b, x1, y1, x2, y2, tau)
        iter_count += 1

        if show_chart:
            plt.plot([a, b], [func(a), func(b)])

    x_result = (a + b) / 2
    y_result = func(x_result)

    if show_chart:
        plt.scatter(x_result, y_result, color='red')

    return y_result, iter_count


def on_count(func, start, end, x1, y1, x2, y2, tau):
    a = start
    b = end

    if y1 <= y2:
        b = x2
        x2 = x1
        y2 = y1
        x1 = b - (tau * (b - a))
        y1 = func(x1)
    else:
        a = x1
        x1 = x2
        y1 = y2
        x2 = b - ((1 - tau) * (b - a))
        y2 = func(x2)

    epsilonN = tau * ((b - a) / 2)

    return a, b, x1, y1, x2, y2, epsilonN
