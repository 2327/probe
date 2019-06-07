#!/usr/bin/env python
"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
"""

from random import random, randint

LIST = []


def gen_list():
    for i in range(201):
        LIST.append(randint(-100,100))
    return LIST


def bubble_sort(list):
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

    return list


print(bubble_sort(gen_list()))
