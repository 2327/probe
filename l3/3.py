#!/usr/bin/env python3
"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

LIST = ['3', '8', '2', '1', '6']
i = 0
j = int(len(LIST)-1)

while i < j:
    try:
        minimum
        maximum
    except:
        minimum = LIST[i]
        maximum = LIST[i]

    if (int(LIST[i]) > int(LIST[i+1])) and (int(LIST[i]) > int(maximum)):
        maximum = LIST[i]
    if (int(LIST[i]) < int(LIST[i+1])) and (int(LIST[i]) < int(minimum)):
        minimum = LIST[i]

    i += 1

print(minimum, maximum)


