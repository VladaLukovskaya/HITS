import sys

for line in sys.stdin:
    data = line.strip().split(' ')
    if len(data) > 3:
        linked_sites = data[3].split(',')
        for site in linked_sites:
            print(f'{data[0]} {data[1]} {data[2]} {data[3]}')
    else:
        print(f'{data[0]} {data[1]} 0  ')
