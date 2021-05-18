import sys

last_site = None
last_linked_sites = ''
hub = 0

for line in sys.stdin:
    line = line.strip().split(' ')
    site = line[0]
    if len(line) > 3:
        linked_sites = line[3]
    else:
        linked_sites = ' '
    if last_site:
        if last_site == site:
            hub += int(line[2])
        else:
            print(f'{last_site} {line[1]} {hub} {last_linked_sites}')
            last_linked_sites = linked_sites
            hub = int(line[2])
    else:
        hub = int(line[2])
        last_linked_sites = linked_sites
    last_site = site

if last_site:
    print(f'{last_site} {line[1]} {hub} {last_linked_sites}')

