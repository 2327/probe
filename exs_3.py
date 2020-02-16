"""
Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны
создаваться по шаблону: “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""
import random

RESULT_LIST = []
RESULT_DICTIONARY = {}
FIRST_NUMBER = 0
SECONDARY_NUMBER = 0

def generate_random_number(start_number=FIRST_NUMBER, end_number=SECONDARY_NUMBER):
    """
    Generate random number exclude null
    """
    result = random.randint(start_number, end_number)
    return generate_random_number() if result == 0 else result


if __name__ == '__main__':
    while True:
        try:
            FIRST_NUMBER = int(input("Введите первое число: "))
            break
        except ValueError:
            print("Введите натуральное число.")

    while True:
        try:
            SECONDARY_NUMBER = int(input("Введите второе число: "))
            break
        except ValueError:
            print("Введите натуральное число.")

    for i in range(FIRST_NUMBER, SECONDARY_NUMBER):
        RESULT_LIST.append(generate_random_number(FIRST_NUMBER, SECONDARY_NUMBER))

    print(f'Result list: {RESULT_LIST}')

    for i, item in enumerate(RESULT_LIST):
        elem = f'elem_{i}'
        RESULT_DICTIONARY[elem] = RESULT_LIST[i]

    print(f'Result list: {RESULT_DICTIONARY}')
