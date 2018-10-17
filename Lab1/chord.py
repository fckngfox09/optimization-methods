import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x_sym = sp.symbols('x')


def default_count(func, x, h=0):
    func_diff = sp.diff(func, x_sym)
    return float(func_diff.subs(x_sym, x))


#
# Метод хорд
#
def count(func, start, end, epsilon, show_chart=False, f_diff_method=default_count):
    a = start
    b = end

    left_diff = f_diff_method(func, a)
    right_diff = f_diff_method(func, b)

    if not (left_diff * right_diff < 0):
        return 'На концах в производной одинаковые знаки'

    x0, y0 = on_count(func, x_sym, a, b, f_diff_method)

    iter_count = 1
    while np.abs(y0) > epsilon:
        if y0 > 0:
            b = x0
        else:
            a = x0

        x_iter, y_iter = on_count(func, x_sym, a, b, f_diff_method)
        x0 = x_iter
        y0 = y_iter
        iter_count += 1

        if show_chart:
            plt.plot([a, b], [func(a), func(b)])

    return func.subs(x_sym, x0), iter_count


def on_count(func, x_sym, start, end, f_diff_method):
    a = start
    b = end

    x_iter = a - (f_diff_method(func, a) * (a - b)) / (f_diff_method(func, a) - f_diff_method(func, b))

    y_iter = f_diff_method(func, x_iter)

    return float(x_iter), float(y_iter)
