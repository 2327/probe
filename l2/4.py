#!/usr/bin/env python3
"""
  Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""

row = [1]
m = row[0]
result = 0

for i in range(5):
    m = m / 2
    if i % 2 == 0:
        n = -m
    else:
        n = m   
    row.append(n)

for i in range(len(row)): 
    result += row[i]

print(result)
