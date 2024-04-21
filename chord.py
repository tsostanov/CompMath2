from tabulate import tabulate
import numpy as np

def chord_method(interval_start, interval_end, initial_guess, epsilon, equation, max_iterations=1000):
    a = interval_start
    b = interval_end
    iterations = 0

    table = [["Итерация", "a", "b", "x_i", "f(a)", "f(b)", "f(x_i)"]]

    while True:
        if iterations >= max_iterations:
            print("Достигнуто максимальное количество итераций. Решение не найдено.")
            return None

        x_i = a - (b - a) * equation(a) / (equation(b) - equation(a))

        table.append([iterations+1, a, b, x_i, equation(a), equation(b), equation(x_i)])

        if abs(equation(x_i)) <= epsilon:
            print("Метод хорд завершен после", iterations+1, "итераций.")
            print("Приближенное значение корня:", x_i)
            print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))
            return x_i

        if np.sign(equation(a)) * np.sign(equation(x_i)) < 0:
            b = x_i
        else:
            a = x_i

        iterations += 1