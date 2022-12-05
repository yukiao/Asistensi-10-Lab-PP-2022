



import re

string=input()
match=re.search(r'^[a-z|02468]{40}[13579\s]{5}$' , string)
if match:
    print('true')
else:
    print('false')