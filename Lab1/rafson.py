import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import newton
import difference_network


x_sym = sp.symbols('x')
func = lambda x: (x * np.arctan(x) - np.log(1 + (x ** 2)) / 2)
arctg_func = x_sym * sp.atan(x_sym) - sp.log(1 + (x_sym ** 2)) / 2


# Построить график функции
def plot_newton_func(start, end, method, x_start, epsilon=0.1):
    plt.figure()
    plt.ion()

    cuts = 1000
    x_arr = np.linspace(start, end, cuts)

    plt.plot(x_arr, func(x_arr))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    method(start, end, epsilon, x_start=x_start)
    plt.draw()
    plt.pause(0.01)
    plt.show()


def newton_method_atan(start, end, epsilon, x_start):
    name = 'Метод Рафсона для 4 задания.'

    y_min, iter_count = newton.rafson_mod(arctg_func, start, end, epsilon, x_start=x_start, show_chart=True)

    print(name, y_min)
    print('Количество итераций ', iter_count)


def newton_method_atan_central_network(start, end, epsilon, x_start):
    name = 'Метод Рафсона для 4 задания, средняя разность.'

    y_min, iter_count = \
        newton.rafson_mod(
            arctg_func,
            start,
            end,
            epsilon,
            show_chart=True,
            f_diff_method=difference_network.central_network,
            f_diff_diff_method=difference_network.central_network_second,
            x_start=x_start)

    print(name, y_min)
    print('Количество итераций ', iter_count)


def newton_method_atan_left_network(start, end, epsilon, x_start):
    name = 'Метод Рафсона для 4 задания. Левая разность.'

    y_min, iter_count = \
        newton.rafson_mod(
            arctg_func,
            start,
            end,
            epsilon,
            show_chart=True,
            f_diff_method=difference_network.left_network,
            f_diff_diff_method=difference_network.central_network_second,
            x_start=x_start)

    print(name, y_min)
    print('Количество итераций ', iter_count)


def newton_method_atan_right_network(start, end, epsilon, x_start):
    name = 'Метод Рафсона для 4 задания. Правая разность.'

    y_min, iter_count = \
        newton.rafson_mod(
            arctg_func,
            start,
            end,
            epsilon,
            show_chart=True,
            f_diff_method=difference_network.right_network,
            f_diff_diff_method=difference_network.central_network_second,
            x_start=x_start)

    print(name, y_min)
    print('Количество итераций ', iter_count)


def find_range_numerically(start, end, epsilon):
    x_arr = np.arange(start, end, 0.01)

    min_a = end
    min_b = start

    timer_emu = 0
    for point in x_arr:
        y_min, iter_count = newton.rafson_mod(arctg_func, start, end, epsilon, x_start=point, show_chart=False)
        if iter_count > 0:
            if point < min_a:
                min_a = point
            if point > min_b:
                min_b = point
        if timer_emu % 5 is 0:
            print('Счёт идёт, никто не заглох...', timer_emu)
        timer_emu += 1

        if (y_min == 'Метод не сошёлся.'):
            return -1,-1

    x_arr = np.arange(min_a, min_b, 0.01)
    plt.plot(x_arr, func(x_arr))

    print('Диапазон начальных значений: [', min_a, ',', min_b, ']')

    return min_a, min_b
