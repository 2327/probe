#!/usr/bin/env python
"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в
другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то
используйте метод сортировки, который не рассматривался на уроках
"""

from random import randint

LIST = []


def gen_list():
    for i in range(2 * int(input('Введите число: ')) + 1):
        LIST.append(randint(0,100))

    return LIST


def merge_sort(list):
    if len(list) > 1:
        mid = int(len(list)) // 2
        lefthalf = list[:mid]
        righthalf = list[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0

        while i < int(len(lefthalf)) and j < int(len(righthalf)):
            if lefthalf[i] < righthalf[j]:
                list[k]=lefthalf[i]
                i=i+1
            else:
                list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < int(len(lefthalf)):
            list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            list[k]=righthalf[j]
            j=j+1
            k=k+1

    return list

print(merge_sort(gen_list()))
