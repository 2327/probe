#!/usr/bin/env python3

LIST = ['-4', '-3', '-7', '-9', '1', '6']
minimum = 0
minimum_index = 0

for i in range(len(LIST)):
    if int(LIST[i]) < 0:
        if int(minimum) > int(LIST[i]):
            minimum = int(LIST[i])
            minimum_index = i

print(minimum, minimum_index)