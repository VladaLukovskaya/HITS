import sys

authority = 0
hub = 0

for line in sys.stdin:
    line = line.strip().split(' ')
    site = line[0]
    links_and_attributes = line[1:]
    linked_to_sites = list()
    if len(links_and_attributes) > 1:
        linked_to_sites.append(links_and_attributes[0])
        hub += int(links_and_attributes[1])
    else:
        authority = int(links_and_attributes[0])
    linked_to_sites = ''.join(linked_to_sites)
    print(f'{site} {str(linked_to_sites)} {authority} {hub}')
