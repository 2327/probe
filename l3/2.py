#!/usr/bin/env python3

LIST1 = ['8', '3', '15', '6', '4', '2']
LIST2 = []

for i in range(len(LIST1)):
    if int(LIST1[i]) % 2 == 0:
        LIST2.append(i)

print(LIST2)
