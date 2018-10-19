import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x_sym = sp.symbols('x')


def default_count(func, x, h=0):
    func_diff = sp.diff(func, x_sym)
    return float(func_diff.subs(x_sym, x))


def default_count_second_der(func, x, h=0):
    func_diff = sp.diff(func, x_sym)
    f_diff_diff = sp.diff(func_diff, x_sym)
    return float(f_diff_diff.subs(x_sym, x))


#
# Метод Ньютона
#
def count(func, start, end, epsilon, show_chart=False, f_diff_method=default_count, f_diff_diff_method=default_count_second_der, x_start=0):
    a = start
    b = end

    left_diff = f_diff_method(func, a)
    right_diff = f_diff_method(func, b)
    if not (left_diff * right_diff < 0):
        return 'На концах в производной одинаковые знаки'

    x0 = x_start
    df = 1
    df_old = df

    iter_count = 1
    while np.abs(df) > epsilon:

        if show_chart:
            plt.scatter(x0, func.subs(x_sym, x0), color='red')

        dff = float(f_diff_diff_method(func, x0))
        df = float(f_diff_method(func, x0))
        x0 -= float(df) / float(dff)

        if iter_count > 0 and np.abs(df) > df_old:
            error = 'Метод не сошёлся.'
            return error, 0

        df_old = np.abs(df)

        iter_count += 1

    return float(func.subs(x_sym, x0)), iter_count


def rafson_mod(func, start, end, epsilon, show_chart=False, f_diff_method=default_count, f_diff_diff_method=default_count_second_der, x_start=0):
    a = start
    b = end

    left_diff = f_diff_method(func, a)
    right_diff = f_diff_method(func, b)
    if not (left_diff * right_diff < 0):
        return 'На концах в производной одинаковые знаки'

    x0 = x_start
    df = 1
    df_old = df

    iter_count = 1
    while np.abs(df) > epsilon:

        if show_chart:
            plt.scatter(x0, func.subs(x_sym, x0), color='red')

        dff = float(f_diff_diff_method(func, x0))
        df = float(f_diff_method(func, x0))
        t = df ** 2 / (df ** 2 + f_diff_method(func, (x0 - float(df) / float(dff))))
        x0 -= t * float(df) / float(dff)

        if iter_count > 0 and np.abs(df) > df_old:
            error = 'Метод не сошёлся.'
            return error, 0

        df_old = np.abs(df)
        iter_count += 1

    return float(func.subs(x_sym, x0)), iter_count


def markvardt_mod(func, start, end, epsilon, show_chart=False, f_diff_method=default_count, f_diff_diff_method=default_count_second_der, x_start=0):
    a = start
    b = end

    left_diff = f_diff_method(func, a)
    right_diff = f_diff_method(func, b)
    if not (left_diff * right_diff < 0):
        return 'На концах в производной одинаковые знаки'

    x0 = x_start
    df = 1

    mu = 10 * float(f_diff_diff_method(func, x0))
    iter_count = 1
    old_iter_count = iter_count

    while np.abs(df) > epsilon:
        df_old = np.abs(df)
        if show_chart:
            plt.scatter(x0, func.subs(x_sym, x0), color='red')

        old_x = x0

        dff = float(f_diff_diff_method(func, old_x))
        df = float(f_diff_method(func, old_x))

        delta = float(df) / (float(dff) + float(mu))
        x0 = old_x - delta

        # Эта проверка не работает, хотя взята с учебника.
        # if func.subs(x_sym, x0) < func.subs(x_sym, old_x):
        #     mu /= 2
        #     iter_count += 1
        # else:
        #     mu *= 2
        #
        if delta > 0:
            mu /= 2
        else:
            mu *= 2

        if iter_count > 0 and np.abs(df) >= df_old:
            error = 'Метод не сошёлся.'
            return error, 0

    return float(func.subs(x_sym, x0)), iter_count
