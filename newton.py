from tabulate import tabulate
from equations import trigonometric_equation1, trigonometric_equation2, cubic_equation
from equations import derivative_trigonometric_equation1, derivative_trigonometric_equation2, derivative_cubic_equation
from equations import dderivative_trigonometric_equation1, dderivative_trigonometric_equation2, \
    dderivative_cubic_equation


def newton_method(interval_start, interval_end, initial_guess, epsilon, equation, max_iterations=1000):
    a = interval_start
    b = interval_end
    iterations = 0
    derivative = globals().get("derivative_" + equation.__name__)
    second_derivative = globals().get("dderivative_" + equation.__name__)

    if equation(a) * second_derivative(a) > 0:
        x_0 = a
    elif equation(b) * second_derivative(b) > 0:
        x_0 = b
    else:
        x_0 = b
        # print("Не удалось выбрать начальное приближение.")
        # return None

    x_i = x_0
    table = [["Итерация", "x_i", "f(x_i)", "f'(x_i)", "x_(i + 1)", "|x_(i + 1) - x_i|"]]

    while True:
        if iterations >= max_iterations:
            print("Достигнуто максимальное количество итераций. Решение не найдено.")
            return None

        f_x_i = equation(x_i)
        f_prime_x_i = derivative(x_i)
        f_double_prime_x_i = second_derivative(x_i)

        x_i_plus_1 = x_i - (f_x_i / f_prime_x_i)
        difference = abs(x_i_plus_1 - x_i)

        table.append([iterations + 1, x_i, f_x_i, f_prime_x_i, x_i_plus_1, difference])

        if abs(f_x_i) <= epsilon or difference <= epsilon:
            print("Метод Ньютона завершен после", iterations + 1, "итераций.")
            print("Приближенное значение корня:", x_i_plus_1)
            print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))
            return x_i_plus_1

        if f_double_prime_x_i == 0:
            print("Производная второго порядка равна нулю. Метод Ньютона не применим.")
            return None

        x_i = x_i_plus_1
        iterations += 1
