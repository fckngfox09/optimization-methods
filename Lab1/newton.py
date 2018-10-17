import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


#
# Метод Ньютона
#
def count(func, f_diff, start, end, epsilon, show_chart=False):
    a = start
    b = end
    x_sym = sp.symbols('x')

    left_diff = float(f_diff.subs(x_sym, a))
    right_diff = float(f_diff.subs(x_sym, b))
    if not (left_diff * right_diff < 0):
        return 'На концах в производной одинаковые знаки'

    x0 = a
    df = float(f_diff.subs(x_sym, x0))

    iter_count = 0
    while np.abs(df) > epsilon:

        if show_chart:
            plt.scatter(x0, func(x0), color='red')

        f_diff_diff = sp.diff(f_diff, x_sym)
        dff = float(f_diff_diff.subs(x_sym, x0))
        x0 -= float(df) / float(dff)
        df = float(f_diff.subs(x_sym, x0))
        iter_count += 1

    return float(func(x0)), iter_count
