fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'

fh = open(fname)
count = 0
lst = list()
for line in fh :
    if line.startswith('From ') == False :
        continue
    f_list = line.split()
    lst.append(f_list[1])
    count = count + 1

for email in lst:
    print(email)
print("There were", count, "lines in the file with From as the first word")
