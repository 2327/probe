#!/usr/bin/env python3
"""
 Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

sequence = input('Введите ряд натуральных чисел:')
n = 0
m = 0

for i in sequence.split(' '):
    if i:
        i = int(i)
        if i > n:
            n = i

for i in range(len(str(n))):
    m += int(str(n)[i])


print('Наибольшее число {}. И сумма чисел {}'.format(n, m))

