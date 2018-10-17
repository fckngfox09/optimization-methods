# Дихотомия
def count(func, start, end, delta, epsilon):
    a = start
    b = end

    x1 = (b + a - delta) / 2
    x2 = (b + a + delta) / 2

    y1 = func(x1)
    y2 = func(x2)

    epsilon_n = (b - a) / 2

    iter_count = 1
    while epsilon_n > epsilon:
        x1, y1, x2, y2, epsilon_n, a, b = on_count(func, a, b, delta, x1, y1, x2, y2)
        iter_count += 1

    x_result = (a + b) / 2
    func_result = func(x_result)

    return func_result, iter_count


def on_count(func, start, end, delta, x1, y1, x2, y2):
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