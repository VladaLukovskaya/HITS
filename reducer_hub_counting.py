#!/usr/bin/python3
import sys

authority = 0.0
hub = 0.0
last_site = ''
site = ''
sites_list = list()
auth_sum = 0.0
hub_sum = 0.0


for line in sys.stdin:
    data = line.strip().split(' ')
    last_site = site
    site = data[0]

    if last_site != site and last_site != '':
        linked_to_sites = ','.join(sites_list)
        hub = round(hub, 3)
        authority = round(authority, 3)
        print(f'{last_site} {linked_to_sites} {authority} {hub}')
        # hub_sum += hub ** 2
        # auth_sum += authority ** 2
        hub = 0
        sites_list = list()

    links_and_attributes = data[1:]

    if len(links_and_attributes) > 1:
        sites_list.append(links_and_attributes[0])
        hub += float(links_and_attributes[1])
    else:
        authority = float(links_and_attributes[0])

linked_to_sites = ','.join(sites_list)
print(f'{last_site} {linked_to_sites} {authority} {hub}')
# auth_sum += authority ** 2
# hub_sum += hub ** 2
# auth_sum = round(auth_sum, 3)
# hub_sum = round(hub_sum, 3)
# print(f'Sums {auth_sum} {hub_sum}')
