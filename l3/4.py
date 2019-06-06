#!/usr/bin/env python3
"""
4. Определить, какое число в массиве встречается чаще всего.
"""

LIST = ['3', '3', '3', '8', '8', '9', '9', '9', '9']
RC = {}
ck = 0
cv = 0

for i in range(len(LIST)):
    try:
        RC[LIST[i]] += 1
    except:
        RC[LIST[i]] = 1

for k,v in RC.items():
    if v > cv:
        ck = k
        cv = v

print('Число {} встречается {} раз'.format(ck,cv))