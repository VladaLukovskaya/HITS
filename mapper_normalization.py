#!/usr/bin/python3
from sys import stdin

auth_sum = 0
hub_sum = 0

for line in stdin:
    data = line.strip().split(' ')
    new_auth = round(float(data[2]) ** 2, 3)
    new_hub = round(float(data[3]) ** 2, 3)
    auth_sum += new_auth
    hub_sum += new_hub
    print(f'{data[0]} {data[1]} {new_auth} {new_hub}')

auth_sum = round(auth_sum, 3)
hub_sum = round(hub_sum, 3)
print(f'000000Sums {auth_sum} {hub_sum}')
