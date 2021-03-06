#!/usr/bin/python3
import sys

authority = 0.0
hub = 0.0
last_site = ''
site = ''
sites_list = list()

for line in sys.stdin:
    data = line.strip().split(' ')
    last_site = site
    site = data[0]

    if last_site != site and last_site != '':
        linked_sites = ','.join(sites_list)
        hub = round(hub, 3)
        authority = round(authority, 3)
        print(f'{last_site} {linked_sites} {authority} {hub}')
        hub = authority = 0.0
        sites_list = list()

    links_and_attributes = data[1:]

    if len(links_and_attributes) > 1:
        sites_list.append(links_and_attributes[0])
        authority += float(links_and_attributes[1])
    else:
        hub = float(links_and_attributes[0])

linked_sites = ','.join(sites_list)
hub = round(hub, 3)
authority = round(authority, 3)
print(f'{last_site} {linked_sites} {authority} {hub}')
