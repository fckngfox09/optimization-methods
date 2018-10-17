import numpy as np


# Метод парабол
def count(func, start, end, epsilon):
    a = start
    b = end

    x1 = a
    x2 = (a + b) / 2
    x3 = b

    f1 = func(x1)
    f2 = func(x2)
    f3 = func(x3)

    x0, x1, x2, x3, f1, f2, f3 = on_count(func, x1, x2, x3, f1, f2, f3)

    while True:
        x_iter, x1, x2, x3, f1, f2, f3 = on_count(func, x1, x2, x3, f1, f2, f3)
        delta = np.abs((x0 - x_iter))
        x0 = x_iter
        if np.abs(delta <= epsilon):
            break

    return func(x0)


def on_count(func, x1, x2, x3, f1, f2, f3):
    a0 = f1
    a1 = (f2 - f1) / (x2 - x1)
    a2 = ((f3 - f1) / (x3 - x1) - (f2 - f1) / (x2 - x1)) / (x3 - x2)

    x = (x1 + x2 - a1 / a2) / 2

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