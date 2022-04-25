input_first_number = int(input("Введите первое число:"))
input_second_number = int(input("Введите второе число:"))

if (input_first_number < input_second_number):
    print("Первое число меньше второго")

elif (input_first_number > input_second_number):
    if (input_first_number > 3 * input_second_number):
        print("Первое число больше второго, больше чем в 3 раза")
    else:
        print("Первое число больше второго")

