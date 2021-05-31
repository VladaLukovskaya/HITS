#!/usr/bin/python3
import sys

for line in sys.stdin:
    data = line.strip().split(' ')
    linked_sites = data[1].split(',')
    for site in linked_sites:
        print(f'{site} {data[0]} {data[3]}')
    print(f'{data[0]} {data[3]}')
