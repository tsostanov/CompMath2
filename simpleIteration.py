from tabulate import tabulate
from equations import trigonometric_equation1, trigonometric_equation2, cubic_equation
from equations import derivative_trigonometric_equation1, derivative_trigonometric_equation2, derivative_cubic_equation
from equations import dderivative_trigonometric_equation1, dderivative_trigonometric_equation2, \
    dderivative_cubic_equation

def derivative_by_definition(func, x, h=0.00001):
    return (func(x + h) - func(x)) / h

def simple_iteration_method(interval_start, interval_end, initial_guess, epsilon, equation, max_iterations=1000):
    a = interval_start
    b = interval_end
    iterations = 0
    derivative = globals().get("derivative_" + equation.__name__)

    max_abs_derivative = max(abs(derivative(a)), abs(derivative(b)))
    lmbda = 1 / max_abs_derivative * ((-1) if (derivative(a) >= 0 and derivative(b) >= 0) else 1)

    def phi(x):
        return x + lmbda * equation(x)

    # Условие сходимости
    max_phi_derivative = max(abs(derivative_by_definition(phi, a)), abs(derivative_by_definition(phi, b)))
    if max_phi_derivative >= 1:
        # print("Метод простой итерации не гарантирует сходимость на данном интервале.")
        # return None
        pass

    iteration_data = []

    while True:
        if iterations > max_iterations:
            print("Достигнуто максимальное количество итераций. Решение не найдено.")
            return None

        f_x = equation(initial_guess)
        next_x = initial_guess + lmbda * f_x

        iteration_data.append({
            "№ итерации": iterations,
            "x_i": initial_guess,
            "φ(x_i)": phi(initial_guess),
            "f(x_i)": f_x,
            "|x_i+1 - x_i|": abs(next_x - initial_guess)
        })

        if abs(next_x - initial_guess) <= epsilon:
            print("Метод завершен после", iterations, "итераций.")
            print("Приближенное значение корня:", next_x)

            headers = "keys"
            print(tabulate(iteration_data, headers=headers, tablefmt="fancy_grid"))
            return next_x

        initial_guess = next_x
        iterations += 1
