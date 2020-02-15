"""
Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться
по шаблону: “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""
import random

result_list = []
result_dictionary = {}

def generate_random_number(start_number, end_number):
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

    result_list.append(generate_random_number(FIRST_NUMBER, SECONDARY_NUMBER))
    print(result_list)
    for i in range(len(result_list)):
        result_dictionary['elem_'] = result_list
    print(result_dictionary)