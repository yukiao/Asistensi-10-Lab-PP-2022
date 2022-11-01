#MENGECEK STRING S
import re

kalimat=input("")
pola="^[a-z\w2468]{40}[13579\s]{5}$"

if(re.findall(pola, kalimat)):
    print("True")
else:
    print("False")

