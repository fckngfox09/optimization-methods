import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
import newton


x_sym = sp.symbols('x')
func = lambda x: (x * np.arctan(x) - np.log(1 + (x ** 2)) / 2)
arctg_func = x_sym * sp.atan(x_sym) - sp.log(1 + (x_sym ** 2)) / 2


def newton_method_atan(start, end, epsilon, x_start):
    name = 'Метод Ньютона для 4 задания.'

    plt.figure()
    plt.ion()

    x_arr = np.arange(start, end, 0.01)

    plt.plot(x_arr, func(x_arr))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    y_min, iter_count = newton.count(arctg_func, start, end, epsilon, x_start=x_start, show_chart=True)
    plt.draw()
    plt.pause(0.01)
    plt.show()
    print(name, y_min)
    print('Количество итераций ', iter_count)


def find_range_numerically(start, end, epsilon):
    name = 'Метод Ньютона для 4 задания.'

    plt.figure()
    plt.ion()

    x_arr = np.arange(start, end, 0.01)

    plt.plot(x_arr, func(x_arr))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    min_a = end
    min_b = start

    timer_emu = 0
    for point in x_arr:
        y_min, iter_count = newton.count(arctg_func, start, end, epsilon, x_start=point, show_chart=True)
        if iter_count > 0:
            if point < min_a:
                min_a = point
            if point > min_b:
                min_b = point
        if timer_emu % 5 is 0:
            print('Счёт идёт, никто не заглох...', timer_emu)
        timer_emu += 1

    print('Диапазон начальных значений: [', min_a, ',', min_b, ']')

    plt.draw()
    plt.pause(0.01)
    plt.show()
    print(name, y_min)
    print('Количество итераций ', iter_count)

    return min_a, min_b
