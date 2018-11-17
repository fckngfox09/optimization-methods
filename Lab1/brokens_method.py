import numpy as np
import sympy as sp
from scipy.optimize import minimize
import difference_network as dn
import matplotlib.pyplot as plt

x_sym = sp.symbols('x')


def count(func, start, end, epsilon, show_chart=False, is_cos=True):
    a = start
    b = end

    f_a = func(a)
    f_b = func(b)
    iter_count = 2

    L = -minimize(lambda x: -np.abs(dn.lambda_central_network(func, x)), a, tol=10**(-5)).fun
    print('LIP: ', L)
    L *= 500
    x_0 = (f_a - f_b + L * (a + b)) / (2 * L)

    y_0 = (f_a + f_b + L * (a - b)) / 2

    pair = []
    pair.append((x_0, y_0))

    delta = (func(x_0) - y_0) / (2 * L)

    while not 2 * L * delta < epsilon:
        delta, pair, x_0 = on_count(func, pair, L)
        iter_count += 1

    y_min = func(x_0)
    iter_count += 1
    plt.scatter(x_0, y_min)

    return y_min


def on_count(func, pair, L):
    x_0, p_0 = pair[0]

    for (x, p) in pair[1:]:
        if p < p_0:
            x_0, p_0 = x, p

    f_x0 = func(x_0)
    delta = (f_x0 - p_0) / L / 2

    x_1 = x_0 - delta
    x_2 = x_0 + delta
    p = (f_x0 + p_0) / 2

    pair.append((x_1, p))
    pair.append((x_2, p))
    pair.remove((x_0, p_0))

    return delta, pair, x_0
