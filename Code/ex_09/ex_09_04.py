name = input('Enter file: ')
if len(name) < 1 : name = 'mbox-short.txt'
handle = open(name)

highSender = None
highCount = 0
emailDict = dict()
for line in handle :
#    print (line.rstrip())
    line = line.rstrip()
    if not line.startswith('From ') :
        continue
    words = line.split()
#    print (words)
    emailDict[words[1]] = emailDict.get(words[1], 0) + 1

for key,value in emailDict.items():
    if highSender is None or value > highCount:
        highSender = key
        highCount = value
print(highSender, highCount)
