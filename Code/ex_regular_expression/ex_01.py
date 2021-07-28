import re

fname = input('Enter file: ')
handle = open(fname)

total = 0
count = 0
for line in handle:
    lst = re.findall('[0-9]+',line)
    if len(lst) < 1:
        continue
    #print('\n',lst)
    for i in lst:
        total = total + int(i)
        #print(int(i), total)
        count = count + 1
print(total)
