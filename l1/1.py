#!/usr/bin/env python3

num = int(input('Ввведите трехзначное число: '))
result = 0
result1 = 1

if num < 100:
    print('Число не трёхзначное!')
    exit(128)

for i in range(len(str(num))):
    result += int(str(num)[i])
    result1 = result1 * int(str(num)[i])

print(result)
print(result1)
