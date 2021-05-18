import sys

sites_dict = dict()

for line in sys.stdin:
    data = line.strip().split(' ')
    if len(data) > 3:
        linked_sites = sites_dict[data[0]] = data[3]
    else:
        linked_sites = sites_dict[data[0]] = ''
    print(f'{data[0]} 0 {data[2]} {sites_dict[data[0]]}')
    linked_sites = linked_sites.split(',')
    new_line = line.strip().replace(' ', ' ')
    for site in linked_sites:
        if site != '':
            print(f'{site} {data[1]} 0')
