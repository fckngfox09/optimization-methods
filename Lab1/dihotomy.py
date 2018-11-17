import matplotlib.pyplot as plt


# Дихотомия
def count(func, start, end, delta, epsilon, show_chart=False):
    a = start
    b = end

    x1 = (b + a - delta) / 2
    x2 = (b + a + delta) / 2

    y1 = func(x1)
    y2 = func(x2)
    iter_count = 2

    epsilon_n = (b - a) / 2

    while epsilon_n > epsilon:
        x1, y1, x2, y2, epsilon_n, a, b = on_count(func, a, b, delta, x1, y1, x2, y2)
        iter_count += 2
        if show_chart:
            plt.plot([a, b], [func(a), func(b)])

    x_result = (a + b) / 2
    func_result = func(x_result)

    if show_chart:
        plt.scatter(x_result, func_result, color='red')

    return func_result, iter_count


def on_count(func, start, end, delta, x1, y1, x2, y2):
    a = start
    b = end

    if y1 <= y2:
        b = x2
    else:
        a = x1

    epsilon_n = ((b - a) / 2)

    x1 = (b + a - delta) / 2
    x2 = (b + a + delta) / 2
    y1 = func(x1)
    y2 = func(x2)

    return x1, y1, x2, y2, epsilon_n, a, b