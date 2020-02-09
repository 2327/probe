"""
Программа выводит все файлы и директории в текущей директории
"""
import os


def print_directory_contents(spath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие файлы во вложенных каталогах.
    """
    for i in os.listdir(spath):
        if os.path.isfile(os.path.join(spath, i)):
            print(f'\\_{i}')
        elif os.path.isdir(os.path.join(spath, i)):
            print_directory_contents(os.path.join(spath, i))
            print(f'- {i} ')


if __name__ == '__main__':
    print_directory_contents('.git')
