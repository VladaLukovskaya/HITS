import sys

# linked_sites = list()
authority = 0
hub = 0

for line in sys.stdin:
    line = line.strip().split(' ')
    site = line[0]
    links_and_attributes = line[1:]
    linked_sites = list()
    if len(links_and_attributes) > 1:
        linked_sites.append(links_and_attributes[0])
        authority += int(links_and_attributes[1])
    else:
        hub = int(links_and_attributes[0])
    linked_sites = ','.join(linked_sites)
    print(f'{site} {str(linked_sites)} {authority} {hub}')
