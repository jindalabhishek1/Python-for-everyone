# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try :
    fh = open(fname)
except :
    print('Cannot open the ' + fname + ' file.')
    quit()
count = 0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    pos0 = line.find ('0')
    snum = line[pos0:]
    inum = float(snum)
    sum = sum + inum
avg = sum / count
print('Average spam confidence:', avg)
