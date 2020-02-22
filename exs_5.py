"""
5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера
(функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям: вывод
первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод всех
подстрок, состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.
"""
import os
FILE = 'file.txt'


def create_file(file):
    """

    """
    if os.path.isfile('file.txt'):
        print('Файл существует')

    with open(file, "w") as file_handler:
        list1 = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        list2 = [i for i in range(1, 33)]

        for i, j in zip(list1, list2):
            file_handler.write(f'{i} {j} \n')

    print_file(file)


def print_file(file):
    """

    """
    with open(file, "r") as file_handler:
        for line in file_handler:
            print(line)


if __name__ == '__main__':
    create_file(FILE)
