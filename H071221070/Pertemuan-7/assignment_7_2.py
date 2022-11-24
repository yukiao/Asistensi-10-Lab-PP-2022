import re

pattern_v4 = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
pattern_v6 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"

jumlah_input = int(input(''))
list_ip = []
for i in range (jumlah_input):
    ip_input = input('')
    list_ip.append(ip_input)


for i in list_ip:
    v4 = re.match(pattern_v4 , i)
    v6 = re.match(pattern_v6 , i)
    if v4:
        print('IPv4')
    elif v6:
        print('IPv6')
    else:
        print('Bukan IP Address')