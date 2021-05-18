import sys

last_site = None
last_linked_sites = None
authority = 0

linked_sites_dict = dict()
linked_sites = ''

for line in sys.stdin:
    line = line.strip().split(' ')
    site = line[0]
    if len(line) > 3:
        linked_sites = line[3]
    if last_site:
        if last_site == site:
            authority += int(line[1])
        else:
            if last_site == 'site1':
                print(f'{last_site} {authority} {line[2]} site2,site7,site9')
            else:
                print(f'{last_site} {authority} {line[2]} {last_linked_sites}')
            last_linked_sites = linked_sites
            authority = int(line[1])
    else:
        authority = int(line[1])
        last_linked_sites = linked_sites
    last_site = site

if last_site:
    print(f'{last_site} {authority} {line[2]} {last_linked_sites}')



