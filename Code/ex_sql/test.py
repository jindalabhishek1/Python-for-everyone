import re

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
lst = []
for line in fh:
    org = re.findall('^From .*@([^ ]*)', line)
    if len(org) != 1: continue
    if org[0] in lst: continue
    lst.append(org[0])

print(lst, len(lst))
