# Сторонние библиотеки.

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

#  Мои модули
import bitwise
import brute_force
import dihotomy
import golden_section
import parabole
import middle_point
import chord
import newton


def main():
    # func = (lambda x: x ** 4 + x ** 2 + x + 1)
    func = (lambda x: x ** 4 + np.exp(-x))
    start = -1
    end = 1
    epsilon = 0.0001

    y_min = brute_force.count(func, start, end, epsilon)
    print('Метод перебора ', y_min)

    delta = 0.005
    y_min = bitwise.count(func, start, end, delta, epsilon)
    print('Поразрядный поиск ', y_min)

    dihotomy_delta = 0.00005
    y_min = dihotomy.count(func, start, end, dihotomy_delta, epsilon)
    print('Дихотомия ', y_min)

    y_min = golden_section.count(func, start, end, epsilon)
    print('Метод золотого сечения', y_min)

    y_min = parabole.count(func, start, end, epsilon)
    print('Метод парабол', y_min)

    # Отсюда начинаются методы, работающие через производные.
    # Как сделать это через lambda я не смог найти.

    start = -1
    end = 1

    x_sym = sp.symbols('x')
    f_diff = sp.diff(x_sym ** 4 + sp.exp(-x_sym), x_sym)
    # f_diff = sp.diff(x_sym ** 4 + x_sym ** 2 + x_sym + 1, x_sym)
    print('Производная ', f_diff)

    y_min = middle_point.count(func, f_diff, start, end, epsilon)
    print('Метод средней точки ', y_min)

    y_min = chord.count(func, f_diff, start, end, epsilon)
    print('Метод хорд', y_min)

    print('Метод Ньютона', newton.count(func, f_diff, start, end, epsilon))


if __name__ == "__main__":
    main()
