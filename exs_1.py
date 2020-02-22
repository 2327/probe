'''
1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением. В функции необходимо
реализовать поиск полного пути по имени файла, а затем «выделение» из этого пути имени файла (без расширения).
'''

import os

FILE = 'gg.txt'


def get_path(sfile):
    """

    """
    for root, dirs, files in os.walk('/tmp'):
        for file in files:
            if file == sfile:
                print(root, file)
                file = file.split(".")
                del file[-1]
                print(''.join(file))


if __name__ == '__main__':
    get_path(FILE)
