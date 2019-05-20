#!/usr/bin/env python3
"""
 Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""

num = int(input('Введите число:'))
result_sum = 0
result_formula = 0

for i in range(1,num+1):
    result_sum += i

result_formula = int(num * ( num + 1 ) / 2)

if result_sum == result_formula:
    print('Равенство верно. Число {}'.format(result_sum,result_formula))
else:
   print('Равенство неверно, но в это условия вы вряд ли когда-либо сможете попасть :)')

