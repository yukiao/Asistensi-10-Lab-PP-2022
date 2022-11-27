import re

def ipv4 (ip):
    pola1 = r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"      # PENJELASAN DI BAWAH
    match1 = fr"{pola1}\.{pola1}\.{pola1}\.{pola1}"         
    return re.fullmatch (match1, ip)

def ipv6 (ip):
    pola2 = r"([0-9A-Fa-f]{1,4}"
    match2 = fr"{pola2}:{pola2}:{pola2}:{pola2}:{pola2}:{pola2}:{pola2}:{pola2}"
    return re.fullmatch (match2, ip)

loop = int(input())
listip = []
for i in range(loop):
    addressip = input()
    listip.append(addressip)
for j in listip:
    if ipv4 (j):
        print("IPv4")
    elif ipv6 (j):
        print("IPv6")
    else:
        ("Bukan IP Address")

# 3 digit, pasti diawali 25, digit ke-3 bisa 0-5
# 3 digit, pasti diawali 2, digit ke-2 bisa 0-4, digit ke-3 bisa 0-9
# 3 digit, pasti diawali 1, digit ke-2 dan 3 bisa 0-9, penulisannya bisa gini 1[0-9][0-9]
# 1/2 digit, yg [1-9] gaada jg gapapa