#!/usr/bin/python3
from sys import stdin

auth_sum = 0.0
hub_sum = 0.0

for elem in stdin:
    line = elem.strip().split(' ')

    if '000000' in line[0] and 'Sum' in line[0]:
        auth_sum = float(line[1]) ** 0.5
        hub_sum = float(line[2]) ** 0.5
    else:
        new_auth = round((float(line[2]) ** 0.5) / auth_sum, 3)
        new_hub = round((float(line[3]) ** 0.5) / hub_sum, 3)
        print(f'{line[0]} {line[1]} {new_auth} {new_hub}')
