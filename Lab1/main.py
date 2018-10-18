# Сторонние библиотеки.

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import seaborn as sns

#  Мои модули
from pip._vendor.distlib.compat import raw_input

import bitwise
import brute_force
import dihotomy
import golden_section
import parabole
import middle_point
import chord
import newton
import difference_network

sns.set()

x_sym = sp.symbols('x')

func = lambda x: (x ** 4 + x ** 2 + x + 1)
# func = (lambda x: x ** 4 + np.exp(-x))

sym_func = x_sym ** 4 + x_sym ** 2 + x_sym + 1
# f = x_sym ** 4 + sp.exp(-x_sym)


# Построить график функции
def plot_func(start, end, method, epsilon=0.1, show_chart=False):
    plt.figure()

    cuts = 1000
    x_arr = np.linspace(start, end, cuts)

    plt.plot(x_arr, func(x_arr))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    method(start, end, epsilon, show_chart)
    plt.show()


def brute_force_method(start, end, epsilon, show_chart):
    y_min = brute_force.count(func, start, end, epsilon, show_chart=show_chart)
    name = 'Метод перебора '
    print(name, y_min)
    plt.title(name)


def bitwise_method(start, end, epsilon, show_chart):
    delta = 0.25
    y_min, iter_count = bitwise.count(func, start, end, delta, epsilon, show_chart=show_chart)
    name = 'Поразрядный поиск '
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def dihotomy_method(start, end, epsilon, show_chart):
    name = 'Дихотомия '
    delta = 0.00005
    y_min, iter_count = dihotomy.count(func, start, end, delta, epsilon, show_chart=show_chart)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def golden_section_method(start, end, epsilon, show_chart):
    name = 'Метод золотого сечения'
    y_min, iter_count = golden_section.count(func, start, end, epsilon, show_chart=show_chart)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def parabole_method(start, end, epsilon, show_chart):
    name = 'Метод парабол '
    y_min, iter_count = parabole.count(func, start, end, epsilon, show_chart=show_chart)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


# Отсюда начинаются методы, работающие через производные.
# Как сделать это через lambda я не смог найти.
def middle_point_method(start, end, epsilon, show_chart):
    name = 'Метод средней точки '
    y_min, iter_count = middle_point.count(sym_func, start, end, epsilon, show_chart=show_chart)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def middle_point_method_central_network(start, end, epsilon, show_chart):
    name = 'Метод средней точки, центральная разность '
    y_min, iter_count = middle_point.count(sym_func, start, end, epsilon, show_chart=show_chart,
                                           f_diff_method=difference_network.central_network)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def middle_point_method_left_network(start, end, epsilon, show_chart):
    name = 'Метод средней точки, левая разность'
    y_min, iter_count = middle_point.count(sym_func, start, end, epsilon, show_chart=show_chart, f_diff_method=difference_network.left_network)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def middle_point_method_right_network(start, end, epsilon, show_chart):
    name = 'Метод средней точки, правая разность '
    y_min, iter_count = middle_point.count(sym_func, start, end, epsilon, show_chart=show_chart,
                                           f_diff_method=difference_network.right_network)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def chord_method(start, end, epsilon, show_chart):
    name = 'Метод хорд'
    y_min, iter_count = chord.count(sym_func, start, end, epsilon, show_chart=show_chart)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def chord_method_central_network(start, end, epsilon, show_chart):
    name = 'Метод хорд, центральная разность '
    y_min, iter_count = chord.count(sym_func, start, end, epsilon, show_chart=show_chart, f_diff_method=difference_network.central_network)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def chord_method_left_network(start, end, epsilon, show_chart):
    name = 'Метод хорд, левая разность '
    y_min, iter_count = chord.count(sym_func, start, end, epsilon, show_chart=show_chart, f_diff_method=difference_network.left_network)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def chord_method_right_network(start, end, epsilon, show_chart):
    name = 'Метод хорд, правая разность '
    y_min, iter_count = chord.count(sym_func, start, end, epsilon, show_chart=show_chart, f_diff_method=difference_network.right_network)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def newton_method(start, end, epsilon, show_chart):
    name = 'Метод Ньютона '
    y_min, iter_count = newton.count(sym_func, start, end, epsilon, show_chart=show_chart)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def newton_method_central_network(start, end, epsilon, show_chart):
    name = 'Метод Ньютона, центральная разность '
    y_min, iter_count = \
        newton.count(
            sym_func,
            start,
            end,
            epsilon,
            show_chart=show_chart,
            f_diff_method=difference_network.central_network,
            f_diff_diff_method=difference_network.central_network_second)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def newton_method_left_network(start, end, epsilon, show_chart):
    name = 'Метод Ньютона, левая разность '
    y_min, iter_count = \
        newton.count(
            sym_func,
            start,
            end,
            epsilon,
            show_chart=show_chart,
            f_diff_method=difference_network.left_network,
            f_diff_diff_method=difference_network.central_network_second)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def newton_method_right_network(start, end, epsilon, show_chart):
    name = 'Метод Ньютона, правая разность '
    y_min, iter_count = \
        newton.count(
            sym_func,
            start,
            end,
            epsilon,
            show_chart=show_chart,
            f_diff_method=difference_network.right_network,
            f_diff_diff_method=difference_network.central_network_second)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def main():
    start = -1
    end = 1
    epsilon = 0.0001
    show_chart = True

    plot_func(start, epsilon, brute_force_method, epsilon, show_chart)
    plot_func(start, epsilon, bitwise_method, epsilon, show_chart)
    plot_func(start, epsilon, dihotomy_method, epsilon, show_chart)
    plot_func(start, epsilon, golden_section_method, epsilon, show_chart)
    plot_func(start, epsilon, parabole_method, epsilon, show_chart)

    plot_func(start, epsilon, middle_point_method, epsilon, show_chart)
    plot_func(start, epsilon, middle_point_method_central_network, epsilon, show_chart)
    plot_func(start, epsilon, middle_point_method_left_network, epsilon, show_chart)
    plot_func(start, epsilon, middle_point_method_right_network, epsilon, show_chart)

    plot_func(start, epsilon, chord_method, epsilon, show_chart)
    plot_func(start, epsilon, chord_method_central_network, epsilon, show_chart)
    plot_func(start, epsilon, chord_method_left_network, epsilon, show_chart)
    plot_func(start, epsilon, chord_method_right_network, epsilon, show_chart)

    plot_func(start, epsilon, newton_method, epsilon, show_chart)
    plot_func(start, epsilon, newton_method_central_network, epsilon, show_chart)
    plot_func(start, epsilon, newton_method_left_network, epsilon, show_chart)
    plot_func(start, epsilon, newton_method_right_network, epsilon, show_chart)


if __name__ == "__main__":
    main()
