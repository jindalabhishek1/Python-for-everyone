fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    print(line.rstrip())
    list = line.split()
    for i in list:
        if lst.count(i) > 0 :
            continue
        lst.append(i)
lst.sort()
print (lst)
