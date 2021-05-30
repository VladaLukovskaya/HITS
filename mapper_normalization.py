from sys import stdin

auth_sum = 0
hub_sum = 0

for line in stdin:
    data = line.strip().split(' ')
    new_auth = float(data[2]) ** 2
    new_hub = float(data[3]) ** 2
    auth_sum += new_auth
    hub_sum += new_hub
    print(f'{data[0]} {data[1]} {new_auth} {new_hub}')

print(f'Sums {auth_sum} {hub_sum}')











# data = stdin.readlines()
# new_data = list()
#
# for elem in data:
#     elem = elem.strip().split(' ')
#     new_data.append(elem)
#
# auth_sum = new_data[-1][-2]
# hub_sum = new_data[-1][-1]
#
# print(f'Sums {auth_sum} {hub_sum}')
#
# for elem in new_data[:-1]:
#     elem = ' '.join(elem)
#     print(elem)
