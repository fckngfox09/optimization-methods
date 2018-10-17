import numpy as np


# Поразрядный поиск
def count(func, start, end, delta, epsilon):
    a = start
    b = end
    d = delta
    y = func(start)

    while np.abs(d * 4) > epsilon:
        a, b, d, y = on_count(func, a, b, d, y)

    return y


def on_count(func, start, end, delta, old_Y):
    a = start
    b = end
    y = old_Y
    a += delta
    y2 = func(a)
    if y2 < y:
        y = y2
    else:
        a = y2
        b = y
        delta /= -4

    return a, b, delta, y
