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
import difference_network
import newton_4_ex
import rafson
import markvardt

sns.set()

x_sym = sp.symbols('x')

func_original = lambda x: (x ** 4 + x ** 2 + x + 1)
# func = (lambda x: x ** 4 + np.exp(-x))
cos_func = lambda x: (np.cos(x) / (x ** 2))
sin_func = lambda x: (x / 10) + (2 * np.sin(4 * x))

sym_func = x_sym ** 4 + x_sym ** 2 + x_sym + 1
# sym_func = x_sym ** 4 + sp.exp(-x_sym)
# sym_func = x_sym * sp.atan(x_sym) - sp.log(1 + (x_sym ** 2)) / 2


# Построить график функции
def plot_func(start, end, method, epsilon=0.1, show_chart=False, func=func_original):
    plt.figure()
    plt.ion()

    cuts = 1000
    x_arr = np.linspace(start, end, cuts)

    plt.plot(x_arr, func(x_arr))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    method(start, end, epsilon, show_chart)
    plt.draw()
    plt.pause(0.01)
    plt.show()


def brute_force_method(start, end, epsilon, show_chart):
    y_min = brute_force.count(func_original, start, end, epsilon, show_chart=show_chart)
    name = 'Метод перебора '
    print(name, y_min)
    plt.title(name)


def bitwise_method(start, end, epsilon, show_chart):
    delta = 0.25
    y_min, iter_count = bitwise.count(func_original, start, end, delta, epsilon, show_chart=show_chart)
    name = 'Поразрядный поиск '
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def dihotomy_method(start, end, epsilon, show_chart):
    name = 'Дихотомия '
    delta = 0.00005
    y_min, iter_count = dihotomy.count(func_original, start, end, delta, epsilon, show_chart=show_chart)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def golden_section_method(start, end, epsilon, show_chart):
    name = 'Метод золотого сечения'
    y_min, iter_count = golden_section.count(func_original, start, end, epsilon, show_chart=show_chart)
    print(name, y_min)
    print('Количество итераций ', iter_count)
    plt.title(name)


def parabole_method(start, end, epsilon, show_chart):
    name = 'Метод парабол '
    y_min, iter_count = parabole.count(func_original, start, end, epsilon, show_chart=show_chart)
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


def newton_method(start, end, epsilon, show_chart, x_start=0):
    name = 'Метод Ньютона '
    y_min, iter_count = newton.count(sym_func, start, end, epsilon, show_chart=show_chart, x_start=x_start)
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


def brute_force_cos(start, end, epsilon, show_chart):
    name = 'Метод перебора для косинуса. '
    y_min = \
        brute_force.count(
            cos_func,
            start,
            end,
            epsilon,
            show_chart)
    print(name, y_min)
    plt.title(name)


def brute_force_sin(start, end, epsilon, show_chart):
    name = 'Метод перебора для косинуса. '
    y_min = \
        brute_force.count(
            sin_func,
            start,
            end,
            epsilon,
            show_chart)
    print(name, y_min)
    plt.title(name)



# ДЛя дебага.
def main():
    start = -1.5
    end = 1.5
    epsilon = 0.0001
    show_chart = True
    #
    # plot_func(start, end, brute_force_method, epsilon, show_chart)
    # plot_func(start, end, bitwise_method, epsilon, show_chart)
    # plot_func(start, end, dihotomy_method, epsilon, show_chart)
    # plot_func(start, end, golden_section_method, epsilon, show_chart)
    # plot_func(start, end, parabole_method, epsilon, show_chart)
    #
    # plot_func(start, end, middle_point_method, epsilon, show_chart)
    # plot_func(start, end, middle_point_method_central_network, epsilon, show_chart)
    # plot_func(start, end, middle_point_method_left_network, epsilon, show_chart)
    # plot_func(start, end, middle_point_method_right_network, epsilon, show_chart)
    #
    # plot_func(start, end, chord_method, epsilon, show_chart)
    # plot_func(start, end, chord_method_central_network, epsilon, show_chart)
    # plot_func(start, end, chord_method_left_network, epsilon, show_chart)
    # plot_func(start, end, chord_method_right_network, epsilon, show_chart)
    #
    # plot_func(start, end, newton_method, epsilon, show_chart)
    # plot_func(start, end, newton_method_central_network, epsilon, show_chart)
    # plot_func(start, end, newton_method_left_network, epsilon, show_chart)
    # plot_func(start, end, newton_method_right_network, epsilon, show_chart)

    # a, b = newton_4_ex.find_range_numerically(start, end, epsilon)
    #
    # newton_4_ex.newton_method_atan(start, end, epsilon, a + 0.01)
    # newton_4_ex.newton_method_atan(start, end, epsilon, a - 0.01)
    # newton_4_ex.newton_method_atan(start, end, epsilon, b + 0.01)
    # newton_4_ex.newton_method_atan(start, end, epsilon, b - 0.01)
    #
    # newton_4_ex.newton_method_atan_central_network(start, end, epsilon, a + 0.01)
    # newton_4_ex.newton_method_atan_central_network(start, end, epsilon, a - 0.01)
    # newton_4_ex.newton_method_atan_central_network(start, end, epsilon, b + 0.01)
    # newton_4_ex.newton_method_atan_central_network(start, end, epsilon, b - 0.01)
    #
    # newton_4_ex.newton_method_atan_left_network(start, end, epsilon, a + 0.01)
    # newton_4_ex.newton_method_atan_left_network(start, end, epsilon, a - 0.01)
    # newton_4_ex.newton_method_atan_left_network(start, end, epsilon, b + 0.01)
    # newton_4_ex.newton_method_atan_left_network(start, end, epsilon, b - 0.01)
    #
    # newton_4_ex.newton_method_atan_right_network(start, end, epsilon, a + 0.01)
    # newton_4_ex.newton_method_atan_right_network(start, end, epsilon, a - 0.01)
    # newton_4_ex.newton_method_atan_right_network(start, end, epsilon, b + 0.01)
    # newton_4_ex.newton_method_atan_right_network(start, end, epsilon, b - 0.01)
    #
    # a, b = rafson.find_range_numerically(start, end, epsilon)
    #
    # rafson.newton_method_atan(start, end, epsilon, a + 0.1)
    # rafson.newton_method_atan(start, end, epsilon, a - 0.1)
    # rafson.newton_method_atan(start, end, epsilon, b + 0.1)
    # rafson.newton_method_atan(start, end, epsilon, b - 0.1)
    #
    # rafson.newton_method_atan_central_network(start, end, epsilon, a + 0.01)
    # rafson.newton_method_atan_central_network(start, end, epsilon, a - 0.1)
    # rafson.newton_method_atan_central_network(start, end, epsilon, b + 0.1)
    # rafson.newton_method_atan_central_network(start, end, epsilon, b - 0.1)
    #
    # rafson.newton_method_atan_left_network(start, end, epsilon, a + 0.1)
    # rafson.newton_method_atan_left_network(start, end, epsilon, a - 0.1)
    # rafson.newton_method_atan_left_network(start, end, epsilon, b + 0.1)
    # rafson.newton_method_atan_left_network(start, end, epsilon, b - 0.1)
    #
    # rafson.newton_method_atan_right_network(start, end, epsilon, a + 0.1)
    # rafson.newton_method_atan_right_network(start, end, epsilon, a - 0.1)
    # rafson.newton_method_atan_right_network(start, end, epsilon, b + 0.1)
    # rafson.newton_method_atan_right_network(start, end, epsilon, b - 0.1)
    #
    # a, b = markvardt.find_range_numerically(start, end, epsilon)
    # #
    # markvardt.newton_method_atan(start, end, epsilon, a + 0.1)
    # markvardt.newton_method_atan(start, end, epsilon, a - 0.1)
    # markvardt.newton_method_atan(start, end, epsilon, b + 0.1)
    # markvardt.newton_method_atan(start, end, epsilon, b - 0.1)
    #
    # markvardt.newton_method_atan_central_network(start, end, epsilon, a + 0.01)
    # markvardt.newton_method_atan_central_network(start, end, epsilon, a - 0.1)
    # markvardt.newton_method_atan_central_network(start, end, epsilon, b + 0.1)
    # markvardt.newton_method_atan_central_network(start, end, epsilon, b - 0.1)
    #
    # markvardt.newton_method_atan_left_network(start, end, epsilon, a + 0.1)
    # markvardt.newton_method_atan_left_network(start, end, epsilon, a - 0.1)
    # markvardt.newton_method_atan_left_network(start, end, epsilon, b + 0.1)
    # markvardt.newton_method_atan_left_network(start, end, epsilon, b - 0.1)
    #
    # markvardt.newton_method_atan_right_network(start, end, epsilon, a + 0.1)
    # markvardt.newton_method_atan_right_network(start, end, epsilon, a - 0.1)
    # markvardt.newton_method_atan_right_network(start, end, epsilon, b + 0.1)
    # markvardt.newton_method_atan_right_network(start, end, epsilon, b - 0.1)


    start = 0
    end = 4
    plot_func(start, end, brute_force_sin, epsilon, func=sin_func)

    start = 1
    end = 12
    plot_func(start, end, brute_force_cos, epsilon, func=cos_func)




if __name__ == "__main__":
    main()
