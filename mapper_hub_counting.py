#!/usr/bin/python3
import sys

for line in sys.stdin:
    data = line.strip().split(' ')
    linked_sites = data[1].split()
    if linked_sites:
        linked_to_sites = linked_sites[0].split(',')
        for site in linked_to_sites:
            print(f'{site} {data[0]} {data[2]}')
    print(f'{data[0]} {data[2]}')
