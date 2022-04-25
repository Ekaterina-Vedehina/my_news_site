import random
import math

print('''
Для генерации чисел введите: random
Для включения калькулятора введите: cal
Для выхода введите 'esc' 
''')
mode = str(input('Режим: '))
if mode == 'random':
    print('"Генерация целых чисел в некотором диапазоне"')
    input_first_number = int(input("Введите границы [левая, правая]:\n левая граница = "))
    input_second_number = int(input("правая граница = "))
    if input_first_number > input_second_number:
        print('Ошибка')
    else:
        print('Рандомное число от ' + str(input_first_number) + ' до ' + str(input_second_number) + ': ' + str(
            random.randint(input_first_number, input_second_number)))

elif mode == 'cal':
    print('''
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
    result = None
    input_first_number = float(input('Число: '))
    action = str(input('Ваше действие: '))
    if action == '+':
        input_second_number = (input('Второе число:'))
        result = input_first_number + input_second_number
    elif action == '-':
        input_second_number = int(input('Второе число:'))
        result = input_first_number - input_second_number
    elif action == '/':
        input_second_number = int(input('Второе число:'))
        result = input_first_number / input_second_number
    elif action == '*':
        input_second_number = int(input('Второе число:'))
        result = input_first_number * input_second_number
    elif action == '^':
        input_second_number = int(input('Степень:'))
        result = input_first_number ** input_second_number
    elif action == 'sqr':
        result = input_first_number ** 2
    elif action == '!':
        result = math.factorial(input_first_number)
    elif action == 'arccos':
        result = math.acos(input_first_number)
    elif action == 'abs':
        result = abs(input_first_number)
    if result is not None:
        print('Результат: ' + str(result))
elif mode == 'esc':
    exit()
else:
    print('Ошибка.')
