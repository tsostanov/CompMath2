import numpy as np
import matplotlib.pyplot as plt
from newton import newton_method
from chord import chord_method
from simpleIteration import simple_iteration_method
from equations import trigonometric_equation1, trigonometric_equation2, cubic_equation
from equations import derivative_trigonometric_equation1, derivative_trigonometric_equation2, derivative_cubic_equation
from equations import dderivative_trigonometric_equation1, dderivative_trigonometric_equation2, \
    dderivative_cubic_equation


def plot_function(equation, interval_start, interval_end):
    x_values = np.linspace(interval_start - 1, interval_end + 1, 1000)
    y_values = equation(x_values)

    plt.plot(x_values, y_values, label=equation.__name__)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции ' + equation.__name__)
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.xlim(interval_start - 1, interval_end + 1)
    plt.ylim(min(y_values) - 1, max(y_values) + 1)
    plt.legend()
    plt.grid(True)
    plt.show()


def verify(interval_start, interval_end, initial_guess, equation):
    if not (isinstance(interval_start, (int, float)) and isinstance(interval_end, (int, float))):
        print("Границы интервала должны быть числами.")
        return False
    if interval_start >= interval_end:
        print("Левая граница интервала должна быть меньше правой.")
        return False
    if (not (isinstance(initial_guess, (int, float)) and interval_start <= initial_guess <= interval_end)
            and initial_guess != 0):
        print("Начальное приближение должно быть числом и находиться между левой и правой границами интервала.")
        return False

    start_value = equation(interval_start)
    end_value = equation(interval_end)

    if np.sign(start_value) * np.sign(end_value) > 0:
        print(
            "На концах интервала функция принимает значения с одним и тем же знаком. Корней на данном интервале "
            "нет (или их четное количество).")
        return False

    derivative_function = globals().get("derivative_" + equation.__name__)

    start_derivative = derivative_function(interval_start)
    end_derivative = derivative_function(interval_end)

    if np.sign(start_derivative) * np.sign(end_derivative) < 0:
        print("Производная функции меняет знак на интервале, поэтому корней может быть несколько.")
        return False
    else:
        print("Производная функции сохраняет знак на интервале, что гарантирует наличие только одного корня.")

    return True


def get_input_from_keyboard():
    interval_start = float(input("Введите начало интервала: "))
    interval_end = float(input("Введите конец интервала: "))
    initial_guess = float(
        input("Введите начальное приближение к корню (ноль, если начальное приближение не требуется): "))
    epsilon = float(input("Введите погрешность вычисления: "))

    return interval_start, interval_end, initial_guess, epsilon


def get_input_from_file():
    while True:
        filename = input("Введите имя файла: ")
        try:
            with open(filename, 'r') as file:
                data = file.readlines()
                interval_start, interval_end, initial_guess, epsilon = map(float, data)
                return interval_start, interval_end, initial_guess, epsilon

        except FileNotFoundError:
            print("Файл не найден. Пожалуйста, убедитесь, что вы ввели правильное имя файла.")


def choose_equation():
    while True:
        print("Выберите уравнение для решения:")
        print("1. Кубическое уравнение: y = x ** 3 - 3.125 * x ** 2 - 3.5 * x + 2.458")
        print("2. Уравнение с тригонометрическими функциями: y = cos(x ** 2) + sin(x)")
        print("3. Еще одно уравнение с тригонометрическими функциями: y = sin(x ** 2) + cos(x)")

        choice = input("Введите номер уравнения (1, 2 или 3): ")

        if choice == '1':
            equation = cubic_equation
            break
        elif choice == '2':
            equation = trigonometric_equation1
            break
        elif choice == '3':
            equation = trigonometric_equation2
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите номер уравнения заново.")

    print("Выберите источник ввода данных:")
    print("1. Ввод с клавиатуры")
    print("2. Чтение данных из файла")

    # input_source = input("Введите номер источника (1 или 2): ")

    while True:
        input_source = input("Выберите источник данных (1 - ввод с клавиатуры, 2 - ввод из файла): ")

        if input_source == '1':
            interval_start, interval_end, initial_guess, epsilon = get_input_from_keyboard()
            break
        elif input_source == '2':
            interval_start, interval_end, initial_guess, epsilon = get_input_from_file()
            break
        else:
            print("Некорректный выбор. Источник данных должен быть 1 или 2.")
            continue

    return equation, interval_start, interval_end, initial_guess, epsilon


def main():
    equation, interval_start, interval_end, initial_guess, epsilon = choose_equation()
    print("Выбранное уравнение:", equation.__name__)
    print("Интервал:", interval_start, "-", interval_end)
    print("Начальное приближение к корню:", initial_guess)
    print("Погрешность вычисления:", epsilon)

    plot_function(equation, interval_start, interval_end)

    if verify(interval_start, interval_end, initial_guess, equation):
        while True:
            print("Выберите метод решения уравнения:")
            print("1. Метод Ньютона")
            print("2. Метод хорд")
            print("3. Метод простых итераций")

            method_choice = input("Введите номер метода (1, 2 или 3): ")

            if method_choice == '1':
                newton_method(interval_start, interval_end, initial_guess, epsilon, equation)
                break
            elif method_choice == '2':
                chord_method(interval_start, interval_end, initial_guess, epsilon, equation)
                break
            elif method_choice == '3':
                simple_iteration_method(interval_start, interval_end, initial_guess, epsilon, equation)
                break
            else:
                print("Некорректный выбор метода. Пожалуйста, введите номер метода от 1 до 3.")


if __name__ == "__main__":
    main()
