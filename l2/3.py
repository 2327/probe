#!/usr/bin/env python3
"""
 Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
"""

def is_int(value):
    try:
        value = int(value)
        if value < 0:
            return('false')
    except:
        return('false')

    return value


while True:
    try:
        num
    except NameError:
        num = None

    if num is None or num == 'false':
        num = is_int(input('Введите положительное число: '))
    if num == 'false' :
        print('Вы ввели некорректное число.\n\n')
        continue
    break

str_num = str(num)
lenght = len(str_num)

print('Зеркальное число: ', end='')
for i in range(lenght):
    lenght -= 1
    print(str_num[lenght], end='')

print('')
