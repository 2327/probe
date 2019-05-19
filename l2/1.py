#!/usr/bin/env python3
"""
 Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""

def is_int(value):
    try:
        value = int(value)
    except:
        return('false')

    return value


def is_operation(value):
    if value != '0' and value != '+' and value != '-' and value != '*' and value != '/':
        return('false')
    return value


while True:
    try:
        num1
        num2
        operation
    except NameError:
        num1 = None
        num2 = None
        operation = None

    if num1 is None or num1 == 'false':
        num1 = is_int(input('Введите первое число: '))
    if num1 == 'false' :
        print('Вы ввели некорректное число.\n\n')
        continue
    if num2 is None or num2 == 'false':
        num2 = is_int(input('Введите второе число: '))
    if num2 == 'false':
        print('Вы ввели некорректное число.\n\n')
        continue

    if operation is None or operation == 'false':
        operation = is_operation(input('Введите действие: '))
    if operation == 'false':
        print('Вы ввели некорректное действие.\n\n')
        continue
    if operation == '0':
      print('Выход из программы.')
      exit(0)
 
    break

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    print('Something anomaly wrong!')

print(result)

