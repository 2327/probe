#!/usr/bin/env python3
"""
 Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
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
even = []
odd = []

for i in range(len(str(num))):
    tmp = int(str(num)[i])
    if tmp % 2 == 0:
        even.append(tmp)
    else:    
        odd.append(tmp)
print('Чётные составляющие' + '(' + str(len(even)) + ')' + ': ', end = '')  
for i in even:
    print(i, ' ', end = '')
print('\nНечётные составляющие' + '(' + str(len(odd)) + ')' + ': ', end = '')
for i in odd:
    print(i, ' ', end = '')

print('')
