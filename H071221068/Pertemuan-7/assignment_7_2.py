#Menentukan IP

import re
n= int(input(""))
listip= []
for i in range(n) :
    ip= input("")
    listip.append(ip)
print(listip)

ipv4= r'^(([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5])\.){3}([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5])$'
ipv6= r'^(([\dA-Fa-f]{1,4}?\:){7})([\dA-Fa-f]{1,4})$'

for j in listip : 
    reasult1= re.match(ipv4, j)
    if reasult1 :
        print("IPv4")
    else :
        reasult2= re.match(ipv6, j)
        if reasult2 :
            print("IPv6")
        else :
            print("Bukan IP Address")