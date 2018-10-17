import numpy as np
import sympy as sp


#
# Метод хорд
#
def count(func, f_diff, start, end, epsilon):
    a = start
    b = end

    x_sym = sp.symbols('x')
    left_diff = f_diff.subs(x_sym, a)
    right_diff = f_diff.subs(x_sym, b)

    if not (left_diff * right_diff < 0):
        return 'На концах в производной одинаковые знаки'

    x0, y0 = on_count(f_diff, x_sym, a, b)

    iter_count = 1
    while np.abs(y0) > epsilon:
        if y0 > 0:
            b = x0
        else:
            a = x0

        x_iter, y_iter = on_count(f_diff, x_sym, a, b)
        x0 = x_iter
        y0 = y_iter
        iter_count += 1

    return func(x0), iter_count


def on_count(f_diff, x_sym, start, end):
    a = start
    b = end

    x_iter = a - (f_diff.subs(x_sym, a) * (a - b)) / (f_diff.subs(x_sym, a) - f_diff.subs(x_sym, b))

    y_iter = f_diff.subs(x_sym, x_iter)

    return float(x_iter), float(y_iter)
