name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

time_dict = dict()
for line in handle :
    if not line.startswith('From ') :
        continue
    words = line.split()
    time = words[5]
    times = time.split(':')
    time_dict[times[0]] = time_dict.get(times[0],0) + 1
#    print (times[0], type(times[0]))

for k,v in sorted(time_dict.items()) :
    print (k, v)
