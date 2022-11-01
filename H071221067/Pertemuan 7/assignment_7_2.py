import re

jumlah_data = int(input('Masukkan jumlah data: '))
IPv4 = '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'
IPv6 = '^(([0-9a-f]|[0-9a-f]{2}|[0-9a-f]{3}|[0-9a-f]{4})\:){7}([0-9a-f]|[0-9a-f]{2}|[0-9a-f]{3}|[0-9a-f]{4})$'
data = []
for i in range (jumlah_data):
    IP_Address = input('Masukkan IP Address: ')
    data.append(IP_Address)
for j in data:
    if re.match(IPv4, j):
        print('IPv4')
    elif re.match(IPv6, j):
        print('IPv6')
    else:
        print('Bukan IP Address')
