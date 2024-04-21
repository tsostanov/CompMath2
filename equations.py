import numpy as np


def cubic_equation(x):
    return x ** 3 - 3.125 * x ** 2 - 3.5 * x + 2.458


def derivative_cubic_equation(x):
    return 3 * x ** 2 - 6.25 * x - 3.5


def dderivative_cubic_equation(x):
    return 6 * x - 6.25


def trigonometric_equation1(x):
    return np.cos(x ** 2) + np.sin(x)


def derivative_trigonometric_equation1(x):
    return np.cos(x) - 2 * x * np.sin(x ** 2)


def dderivative_trigonometric_equation1(x):
    return -2 * np.sin(x ** 2) - 4 * x ** 2 * np.cos(x ** 2) - np.sin(x)


def trigonometric_equation2(x):
    return np.sin(x ** 2) + np.cos(x)


def derivative_trigonometric_equation2(x):
    return 2 * x * np.cos(x ** 2) - np.sin(x)


def dderivative_trigonometric_equation2(x):
    return 2 * np.cos(x ** 2) - np.cos(x) - 4 * x ** 2 * np.sin(x ** 2)
