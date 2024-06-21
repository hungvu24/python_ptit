import re
s = input()
match = re.search(r'\.py$',s)
if match:
    print('yes')
else :
    print('no')