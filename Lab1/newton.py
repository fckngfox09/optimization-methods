import sympy as sp
import numpy as np


#
# Метод Ньютона
#
def count(func, f_diff, start, end, epsilon):
    a = start
    b = end
    x_sym = sp.symbols('x')

    left_diff = f_diff.subs(x_sym, a)
    right_diff = f_diff.subs(x_sym, b)
    if not (left_diff * right_diff < 0):
        return 'На концах в производной одинаковые знаки'

    x0 = a
    df = f_diff.subs(x_sym, x0)

    while np.abs(df) > epsilon:
        f_diff_diff = sp.diff(f_diff, x_sym)
        dff = f_diff_diff.subs(x_sym, x0)
        x0 -= df / dff
        df = f_diff.subs(x_sym, x0)

    return float(func(x0))