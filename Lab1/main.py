import numpy as np
import sympy as sp
from sympy.abc import x
import math as m
import matplotlib.pyplot as plt


# Метод перебора
def bruteForce(func, start, end, epsilon):
    a = start
    b = end
    n = (b - a) / epsilon
    x = np.linspace(a, b, n)
    y = func(x)

    minimum = np.min(y)
    return minimum


# Поразрядный поиск
def bitwiseSearch(func, start, end, delta, epsilon):
    a = start
    b = end
    d = delta
    y = func(start)

    while np.abs(d * 4) > epsilon:
        a, b, d, y = onBitwiseSearch(func, a, b, d, y)

    return y


def onBitwiseSearch(func, start, end, delta, old_Y):
    a = start
    b = end
    y = old_Y
    a += delta
    y2 = func(a)
    if y2 < y:
        y = y2
    else:
        a = y2
        b = y
        delta /= -4

    return a, b, delta, y


# Дихотомия
def dihotomy(func, start, end, delta, epsilon):
    a = start
    b = end

    x1 = (b + a - delta) / 2
    x2 = (b + a + delta) / 2

    y1 = func(x1)
    y2 = func(x2)

    epsilonN = (b - a) / 2

    while epsilonN > epsilon:
        x1, y1, x2, y2, epsilonN, a, b = onDihotomy(func, a, b, delta, x1, y1, x2, y2)

    xResult = (a + b) / 2
    funcResult = func(xResult)
    return funcResult


def onDihotomy(func, start, end, delta, x1, y1, x2, y2):
    a = start
    b = end

    if y1 <= y2:
        b = x2
    else:
        a = x1

    epsilonN = ((b - a) / 2)

    x1 = (b + a - delta) / 2
    x2 = (b + a + delta) / 2
    y1 = func(x1)
    y2 = func(x2)

    return x1, y1, x2, y2, epsilonN, a, b


# Метод золотого сечения
def goldenSectionMethod(func, start, end, epsilon):
    a = start
    b = end

    x1 = a + ((3 - np.sqrt(5)) / 2) * (b - a)
    x2 = a + ((np.sqrt(5) - 1) / 2) * (b - a)

    y1 = func(x1)
    y2 = func(x2)

    tau = (np.sqrt(5) - 1) / 2
    epsilonN = (b - a) / 2

    while epsilonN > epsilon:
        a, b, x1, y1, x2, y2, epsilonN = onGoldenSectionMethod(func, a, b, x1, y1, x2, y2, tau)

    xResult = (a + b) / 2
    yResult = func(xResult)
    return yResult


def onGoldenSectionMethod(func, start, end, x1, y1, x2, y2, tau):
    a = start
    b = end

    if y1 <= y2:
        b = x2
        x2 = x1
        y2 = y1
        x1 = b - (tau * (b - a))
        y1 = func(x1)
    else:
        a = x1
        x1 = x2
        y1 = y2
        x2 = b - ((1 - tau) * (b - a))
        y2 = func(x2)

    epsilonN = tau * ((b - a) / 2)

    return a, b, x1, y1, x2, y2, epsilonN


# Метод парабол
def parabole(func, start, end, epsilon):
    a = start
    b = end

    x1 = a
    x2 = (a + b) / 2
    x3 = b

    f1 = func(x1)
    f2 = func(x2)
    f3 = func(x3)

    x0, x1, x2, x3, f1, f2, f3 = onParabole(func, x1, x2, x3, f1, f2, f3)

    while True:
        x_iter, x1, x2, x3, f1, f2, f3 = onParabole(func, x1, x2, x3, f1, f2, f3)
        delta = np.abs((x0 - x_iter))
        x0 = x_iter
        if np.abs(delta <= epsilon):
            break

    return func(x0)


def onParabole(func, x1, x2, x3, f1, f2, f3):
    a0 = f1
    a1 = (f2 - f1) / (x2 - x1)
    a2 = ((f3 - f1) / (x3 - x1) - (f2 - f1) / (x2 - x1)) / (x3 - x2)

    x = (x1 + x2 - a1 / a2) / 2

    fx = func(x)

    if x > x2 and fx > f2:
        x3, f3 = x, fx
    elif x > x2 and fx < f2:
        x1, f1 = x2, f2
        x2, f2 = x, fx
    elif x < x2 and fx > f2:
        x1, f1 = x, fx
    elif x < x2 and fx < f2:
        x3, f3 = x2, f2
        x2, f2 = x, fx

    return x, x1, x2, x3, f1, f2, f3


# Метод средней точки
def middlePoint(func, f_diff, start, end, epsilon):
    a = start
    b = end
    x_sym = sp.symbols('x')

    left_diff = f_diff.subs(x_sym, a)
    right_diff = f_diff.subs(x_sym, b)

    if not ((left_diff > 0 > right_diff) or (right_diff > 0 > left_diff)):
        return 'На концах в производной одинаковые знаки.'

    df, x0 = on_middle_point(f_diff, x_sym, a, b)

    while np.abs(df) > epsilon:
        if df > 0:
            b = x0
        else:
            a = x0

        df, x1 = on_middle_point(f_diff, x_sym, a, b)
        x0 = x1

    return func(x0)


def on_middle_point(f_diff, x_sym, start, end):
    a = start
    b = end

    x_iter = (a + b) / 2
    df = f_diff.subs(x_sym, x_iter)

    return df, x_iter


def chord_method():
    return


def main():
    func = (lambda x: x ** 4 + x ** 2 + x + 1)
    # func = (lambda x: x ** 4 + np.exp(-x))
    start = -1
    end = 1
    epsilon = 0.001

    print('Метод перебора ', bruteForce(func, start, end, epsilon))

    delta = 0.005
    print('Поразрядный поиск ', bitwiseSearch(func, start, end, delta, epsilon))

    dihotomyDelta = 0.00005
    print('Дихотомия ', dihotomy(func, start, end, dihotomyDelta, epsilon))

    print('Метод золотого сечения', goldenSectionMethod(func, start, end, epsilon))

    print('Метод парабол', parabole(func, start, end, epsilon))

    # Отсюда начинаются методы, работающие через производные.
    # Как сделать это через lambda я не смог найти.

    start = 0
    end = 1

    x_sym = sp.symbols('x')
    # f_diff = sp.diff(x ** 4 + sp.exp(-x), x)
    f_diff = sp.diff(x_sym ** 4 + x_sym ** 2 + x_sym + 1, x_sym)
    print('Производная ', f_diff)
    print('Метод средней точки ', middlePoint(func, f_diff, start, end, epsilon))

    plt.figure()


if __name__ == "__main__":
    main()
