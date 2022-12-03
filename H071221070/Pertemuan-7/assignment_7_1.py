import re

string = input('')
pattern = '^[a-zA-Z2468]{40}[\s13579]{5}$'
match = re.search(pattern, string)

if match:
    print('true')
else:
    print('false')