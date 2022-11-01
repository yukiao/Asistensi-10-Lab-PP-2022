import re

s = input('Masukkan inputan: ')
pattern = '^[A-Za-z2468]{40}[\s13579]{5}$'

if re.match(pattern, s):
    print('True')
else:
    print('False')