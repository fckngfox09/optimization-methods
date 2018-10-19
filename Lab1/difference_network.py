import sympy as sp

x_sym = sp.symbols('x')


def left_network(func, x, h=0.001):
    return (func.subs(x_sym, x) - func.subs(x_sym, (x - h))) / h


def right_network(func, x, h=0.001):
    return (func.subs(x_sym, (x + h)) - func.subs(x_sym, x)) / h


def central_network(func, x, h=0.001):
    return (func.subs(x_sym, (x + h)) - func.subs(x_sym, (x - h))) / (2 * h)


def lambda_central_network(func, x, h=0.001):
    return (func(x + h) - func(x - h)) / (2 * h)


def central_network_second(func, x, h=0.001):
    return (func.subs(x_sym, (x + h)) - 2 * func.subs(x_sym, x) + func.subs(x_sym, (x - h))) / (h ** 2)
