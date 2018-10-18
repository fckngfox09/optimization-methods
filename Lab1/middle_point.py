import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


x_sym = sp.symbols('x')


def default_count(func, x, h=0):
    func_diff = sp.diff(func, x_sym)
    return func_diff.subs(x_sym, x)


# Метод средней точки
def count(func, start, end, epsilon, show_chart=False, f_diff_method=default_count):
    a = start
    b = end

    left_diff = f_diff_method(func, a)
    right_diff = f_diff_method(func, b)

    if not (left_diff * right_diff < 0):
        return 'На концах в производной одинаковые знаки.'

    df, x0 = on_count(f_diff_method, func, a, b)

    iter_count = 1
    step = 0.2
    while np.abs(df) > epsilon:
        if df > 0:
            b = x0
        else:
            a = x0

        df, x1 = on_count(f_diff_method, func, a, b)

        if show_chart:
            x_p = np.linspace(x1 - step, x1 + step, 200)
            plt.plot(x_p, df * (x_p - x1) + func(x1))

        x0 = x1
        iter_count += 1

    if show_chart:
        plt.scatter(x0, func.subs(x_sym, x0), color='red')

    return func.subs(x_sym, x0), iter_count


def on_count(f_diff_method, func, start, end):
    a = start
    b = end

    x_iter = (a + b) / 2
    df = f_diff_method(func, x_iter)

    return df, x_iter
