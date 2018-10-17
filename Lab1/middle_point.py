import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# Метод средней точки
def count(func, f_diff, start, end, epsilon, show_chart=False):
    a = start
    b = end
    x_sym = sp.symbols('x')

    left_diff = f_diff.subs(x_sym, a)
    right_diff = f_diff.subs(x_sym, b)

    if not (left_diff * right_diff < 0):
        return 'На концах в производной одинаковые знаки.'

    df, x0 = on_count(f_diff, x_sym, a, b)

    iter_count = 1
    step = 0.25
    while np.abs(df) > epsilon:
        if df > 0:
            b = x0
        else:
            a = x0

        x_p = np.linspace(x0 + step, x0 - step, 200)

        df, x1 = on_count(f_diff, x_sym, a, b)

        if show_chart:
            plt.plot(x_p, df * (x_p - x0) + func(x0))

        x0 = x1
        iter_count += 1

    return func(x0), iter_count


def on_count(f_diff, x_sym, start, end):
    a = start
    b = end

    x_iter = (a + b) / 2
    df = f_diff.subs(x_sym, x_iter)

    return df, x_iter
