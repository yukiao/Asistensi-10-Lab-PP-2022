import re

string_s=input('masukkan string s :')
match=re.match("^[24068a-zA-Z]{40}[13579\s]{5}$",string_s)
if match :
    print("true")
else:
    print("false")    