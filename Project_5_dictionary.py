input_first_list = input('Введите список слов через запятую: ').split(',')
first_list = list()
for el in input_first_list:
    if el == '':
        continue
    for i in el:
        if i == ' ':
            el = el.replace(' ', '')
    first_list.append(el)
first_set = set(first_list)
length_first_set = len(first_set)
print('Первый список имеет ' + str(length_first_set) +
      ' слов(а). Сформируйте второй список с таким же количествои слов.')

input_second_list = input('Введите список слов через запятую: ').split(',')
second_list = list()
for el in input_second_list:
    if el == '':
        continue
    for i in el:
        if i == ' ':
            el = el.replace(' ', '')
    second_list.append(el)
second_set = set(second_list)
length_second_set = len(second_set)


if length_first_set == length_second_set:
    dictionary = dict(zip(first_set, second_set))
    print(dictionary)
else:
    print('Ошибка. Количество слов не совпадает. Попробуйте заново.')
