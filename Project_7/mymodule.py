import random
import math


def help_text(numbers):
    if numbers == '1':
        print('''
        Для генерации чисел введите: random
        Для включения калькулятора введите: cal
        Для выхода введите 'esc' 
        ''')
    elif numbers == '2':
        print('''
        ____________________________________
        Функционал:
         Сложение: +
         Вычитание: -
         Деление: /
         Умножение: *
         Модуль: abs
         Возведение во 2 степень: sqr
         Возведение во n-ую целую степень: ^
         Факториал: !
         Арккосинус (–1 ≤ x ≤ 1): arccos
        ____________________________________''')
    else:
        print('Результат: ' + str(numbers))


def number_generation():
    print('"Генерация целых чисел в некотором диапазоне"')
    input_first_number = int(input("Введите границы [левая, правая]:\n левая граница = "))
    input_second_number = int(input("правая граница = "))
    if input_first_number > input_second_number:
        print('Ошибка')
    else:
        print('Рандомное число от ' + str(input_first_number) + ' до ' + str(input_second_number) + ': ' + str(
            random.randint(input_first_number, input_second_number)))


def add(num1):
    num2 = float(input('Второе число:'))
    res = num1 + num2
    return res


def subtraction(num1):
    num2 = float(input('Второе число:'))
    res = num1 - num2
    return res


def division(num1):
    num2 = float(input('Второе число:'))
    if num2 == 0:
        res = 'Ошибка. Деление на 0.'
        return res
    else:
        res = num1 / num2
    return res


def multiplication(num1):
    num2 = int(input('Второе число:'))
    res = num1 * num2
    return res


def power(num1):
    num2 = int(input('Степень:'))
    res = num1 ** num2
    return res


def sqr(num1):
    res = num1 ** 2
    return res


def calculator():
    result = None
    input_first_number = float(input('Число: '))
    action = str(input('Ваше действие: '))
    if action == '+':
        result = add(input_first_number)
    elif action == '-':
        result = subtraction(input_first_number)
    elif action == '/':
        result = division(input_first_number)
    elif action == '*':
        result = multiplication(input_first_number)
    elif action == '^':
        result = power(input_first_number)
    elif action == 'sqr':
        result = sqr(input_first_number)
    elif action == '!':
        result = math.factorial(input_first_number)
    elif action == 'arccos':
        result = math.acos(input_first_number)
    elif action == 'abs':
        result = abs(input_first_number)
    if result is not None:
        help_text(result)
    return result
