import mymodule

mymodule.help_text('1')
mode = str(input('Режим: '))
if mode == 'random':
    mymodule.number_generation()
elif mode == 'cal':
    mymodule.help_text('2')
    mymodule.calculator()
elif mode == 'esc':
    exit()
else:
    print('Ошибка.')
