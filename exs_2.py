"""
Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и
после запятой. Если они совпадают, программа должна возвращать
значение True, иначе False.
"""


def number_check(number):
    """
        Функция работет с введенным числом
    """
    if float(number).is_integer():
        print('Введено целое число')
        result = False
    else:
        number_parts = str(number).split('.')
        if number_parts[0] > number_parts[1]:
            print('Введено дробное число. Целая часть больше')
            result = False
        elif number_parts[0] < number_parts[1]:
            print('Введено дробное число. Целая часть меньше')
            result = False
        else:
            print('Введено дробное число. Целая часть равно дробной')
            result = True

    return result


if __name__ == '__main__':
    while True:
        try:
            NUMBER = float(input("Введите число: "))
            break
        except ValueError:
            print("Неверный ввод. Введите число.")

    print(number_check(NUMBER))
