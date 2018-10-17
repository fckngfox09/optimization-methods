# Сторонние библиотеки.

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import seaborn as sns

#  Мои модули
import bitwise
import brute_force
import dihotomy
import golden_section
import parabole
import middle_point
import chord
import newton

sns.set()


# Построить график функции
def plot_func(func, start, end):
    plt.figure()

    cuts = 1000
    x_arr = np.linspace(start, end, cuts)

    plt.plot(x_arr, func(x_arr))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)


def main():
    # func = (lambda x: x ** 4 + x ** 2 + x + 1)
    func = (lambda x: x ** 4 + np.exp(-x))
    start = -1
    end = 1
    epsilon = 0.0001
    plot_func(func, start, end)

    epsilon_for_showing = 0.1
    y_min = brute_force.count(func, start, end, epsilon)
    print('Метод перебора ', y_min)

    delta = 0.25
    y_min, iter_count = bitwise.count(func, start, end, delta, epsilon)
    print('Поразрядный поиск ', y_min)
    print('Количество итераций ', iter_count)

    dihotomy_delta = 0.00005
    y_min, iter_count = dihotomy.count(func, start, end, dihotomy_delta, epsilon)
    print('Дихотомия ', y_min)
    print('Количество итераций ', iter_count)
    plt.show()

    y_min, iter_count = golden_section.count(func, start, end, epsilon)
    print('Метод золотого сечения', y_min)
    print('Количество итераций ', iter_count)

    y_min, iter_count = parabole.count(func, start, end, epsilon)
    print('Метод парабол', y_min)
    print('Количество итераций ', iter_count)

    # Отсюда начинаются методы, работающие через производные.
    # Как сделать это через lambda я не смог найти.

    start = -1
    end = 1

    x_sym = sp.symbols('x')
    f_diff = sp.diff(x_sym ** 4 + sp.exp(-x_sym), x_sym)
    # f_diff = sp.diff(x_sym ** 4 + x_sym ** 2 + x_sym + 1, x_sym)
    print('Производная ', f_diff)

    y_min, iter_count = middle_point.count(func, f_diff, start, end, epsilon)
    print('Метод средней точки ', y_min)
    print('Количество итераций ', iter_count)

    y_min, iter_count = chord.count(func, f_diff, start, end, epsilon)
    print('Метод хорд', y_min)
    print('Количество итераций ', iter_count)

    y_min, iter_count = newton.count(func, f_diff, start, end, epsilon)
    print('Метод Ньютона', y_min)
    print('Количество итераций ', iter_count)


if __name__ == "__main__":
    main()
