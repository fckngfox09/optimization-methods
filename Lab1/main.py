import numpy as np
import matplotlib.pyplot as plt


# Метод перебора
def bruteForce(func, start, end, epsilon):
    a = start
    b = end
    n = (b - a) / epsilon
    x = np.linspace(a, b, n)
    y = func(x)

    minimum = np.min(y)
    print(minimum)


# Поразрядный поиск
def bitwiseSearch(func, start, end, delta, epsilon):
    a = start
    b = end
    d = delta
    y = func(start)

    while np.abs(d * 4) > epsilon:
        a, b, d, y = onBitwiseSearch(func, a, b, d, epsilon, y)

    return y


def onBitwiseSearch(func, start, end, delta, epsilon, old_Y):
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
        x1, y1, x2, y2, epsilonN, a, b = onDihotomy(func, a, b, delta, epsilon, x1, y1, x2, y2)

    xResult = (a + b) / 2
    funcResult = func(xResult)
    return funcResult


def onDihotomy(func, start, end, delta, epsilon, x1, y1, x2, y2):
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

    return onGoldenSectionMethod(func, a, b, epsilon, x1, y1, x2, y2, tau)


def onGoldenSectionMethod(func, start, end, epsilon, x1, y1, x2, y2, tau):
    a = start
    b = end
    epsilonN = (b - a) / 2

    if epsilonN > epsilon:
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
        return onGoldenSectionMethod(func, a, b, epsilon, x1, y1, x2, y2, tau)
    else:
        xResult = (a + b) / 2
        yResult = func(xResult)
        return yResult


def main():
    # func = (lambda x: x ** 4 + x ** 2 + x + 1)
    # func = (lambda x: x ** 2)
    func = (lambda  x: x ** 4 + np.exp(-x))
    start = 0

    end = 1
    epsilon = 0.0001
    print('Метод перебора ')
    bruteForce(func, start, end, epsilon)

    delta = 0.005
    print('Поразрядный поиск ', bitwiseSearch(func, start, end, delta, epsilon))

    dihotomyDelta = 0.00005
    print('Дихотомия ', dihotomy(func, start, end, dihotomyDelta, epsilon))

    print('Метод золотого сечения', goldenSectionMethod(func, start, end, epsilon))


if __name__ == "__main__":
    main()
