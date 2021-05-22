import sys

authority = 0
hub = 0
last_site = ''
site = ''
sites_list = list()

for line in sys.stdin:
    data = line.strip().split(' ')
    last_site = site
    site = data[0]

    if last_site != site and last_site != '':
        linked_sites = ','.join(sites_list)
        print(f'{last_site} {linked_sites} {authority} {hub}')
        hub = authority = 0
        sites_list = list()

    links_and_attributes = data[1:]

    if len(links_and_attributes) > 1:
        sites_list.append(links_and_attributes[0])
        authority += int(links_and_attributes[1])
    else:
        hub = int(links_and_attributes[0])

linked_sites = ','.join(sites_list)
print(f'{last_site} {linked_sites} {authority} {hub}')
