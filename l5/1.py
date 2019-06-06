#!/usr/bin/env python3
"""
  1. Пользователь вводит данные о количестве предприятий, их наименования и
  прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
  Программа должна определить среднюю прибыль (за год для всех предприятий)
  и вывести наименования предприятий, чья прибыль выше среднего и отдельно
  вывести наименования предприятий, чья прибыль ниже среднего.
"""

QUANTITY_FIRMS = int(input('Введите количество предприятий: '))
FIRMS = {}
PROFIT = {}
j=0

print('Всего предприятий: {} \n'.format(QUANTITY_FIRMS))

for i in range(QUANTITY_FIRMS):
    FIRM = input('Введите наименование предприятия {}: '.format(i+1))

    while j < 4:
        PROFIT['quarter'] = input('Введите прибыль за квартал {}: '.format(j + 1))
        try:
            PROFIT['total'] += int(PROFIT['quarter'])
        except KeyError:
            PROFIT['total'] = int(PROFIT['quarter'])

        j += 1

    PROFIT['average'] = int(PROFIT['total']) / 4

    FIRMS[FIRM] = PROFIT
    j=0
    PROFIT = {}

print(FIRMS)
