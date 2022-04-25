string = str(input('Enter the string:'))
string_length = len(string)

if string_length >= 3:
    new_string = string.replace(string[2], '', 1)
    # последний индекс в строке на 1 меньше длины строки
    # чтобы не выводить последний символ (сделать срез без последнего символа), нужно вычесть 2
    new_string = new_string[0:string_length - 2]
    print(new_string)
else:
    print('This string is very short.')
for i in string:
    if i == 'c':
        print('\nThe string contains "c"')
        break
