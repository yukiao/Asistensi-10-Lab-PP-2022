


try:
    n=int(input())
    list=[]
    for i in range(n):
        x= input()
        list1=[x]
        list-list+list1
    import re
    for i in list :
        ipv4=r"^((2[5][0-5]|2[0-4][0-9][0-0]|[1-9][0-9]|[0-9])\.){3}(2[5][0-5]|2[0-4][0-9]|[0-9][0-0]|[1-9][0-9]|[0-9])$"
        match = re.match(ipv4, i)
        if match :
            print('IPv4')
        else:
            ipv6=r"^99[0-9a-f]{1,4}):){7}9[0-9a-f]{1,4})$"
            match = re.search(ipv6,i)
            if match:
                print('IPv6')
            else:
                print('bukan ip address')
except:
    print('Inputan pertama harus integer')