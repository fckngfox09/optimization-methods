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

    print('Метод перебора ', brute_force.count(func, start, end, epsilon))

    delta = 0.005
    print('Поразрядный поиск ', bitwise.count(func, start, end, delta, epsilon))

    dihotomyDelta = 0.00005
    print('Дихотомия ', dihotomy.count(func, start, end, dihotomyDelta, epsilon))

    print('Метод золотого сечения', golden_section.count(func, start, end, epsilon))

    print('Метод парабол', parabole.count(func, start, end, epsilon))

    # Отсюда начинаются методы, работающие через производные.
    # Как сделать это через lambda я не смог найти.

    start = -1
    end = 1

    x_sym = sp.symbols('x')
    f_diff = sp.diff(x_sym ** 4 + sp.exp(-x_sym), x_sym)
    # f_diff = sp.diff(x_sym ** 4 + x_sym ** 2 + x_sym + 1, x_sym)
    print('Производная ', f_diff)
    print('Метод средней точки ', middle_point.count(func, f_diff, start, end, epsilon))
    print('Метод хорд', chord.count(func, f_diff, start, end, epsilon))
    print('Метод Ньютона', newton.count(func, f_diff, start, end, epsilon))


if __name__ == "__main__":
    main()
