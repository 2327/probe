#!/usr/bin/env python
"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

from random import random, randint

LIST = []

def gen_list():
    for i in range(10):
        LIST.append(randint(0,100))
    return LIST


def merge_sort(list):
    try:
        list
    except:
        print('Something went wrong. Emergency stop...')
        exit(0)

    lap = True

    print(list)

    while lap:
        lap = False
        i = 0
        while i < int(len(list) - 1):
            if int(list[i]) > int(list[i + 1]):
                list[i], list[i + 1] = list[i + 1], list[i]
                lap = True
            i += 1

    return(list0, list1)


print(bubble_sort(gen_list()))
