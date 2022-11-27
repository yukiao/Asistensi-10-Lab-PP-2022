import re

string = input("Masukkan string S : ")
pattern = re.match("^[a-zA-Z2468]{40}[13579\s]{5}$", string)
if pattern:
    print("true")
else:
    print("false")

# 2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57